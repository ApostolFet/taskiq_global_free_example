from dishka.integrations.taskiq import inject, FromDishka
from taskiq import AsyncBroker

from my_app.interfaces import Strategy

@inject
async def my_task(strategy: FromDishka[Strategy]) -> int:
    result = await strategy()
    return result

def register_tasks(broker: AsyncBroker):
    broker.register_task(my_task)
