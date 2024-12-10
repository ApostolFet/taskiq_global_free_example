from contextlib import asynccontextmanager
from dishka import make_async_container
from dishka.integrations.fastapi import FromDishka, inject, setup_dishka
from fastapi import  APIRouter, FastAPI

from my_app.interfaces import DoTask
from my_app.providers import DoTaskProvider

router = APIRouter()


@router.post("/")
@inject
async def run_task(do_task: FromDishka[DoTask]) -> str:
    return await do_task()

@router.get("/")
@inject
async def get_result_task(task_id: str, do_task: FromDishka[DoTask]) -> int:
    return await do_task.get_result(task_id)

@asynccontextmanager
async def lifespan(app: FastAPI):
    yield
    await app.state.dishka_container.close()

def create_app() -> FastAPI:
    app = FastAPI(lifespan=lifespan)
    app.include_router(router)
    container = make_async_container(DoTaskProvider())
    setup_dishka(container, app)
    return app
