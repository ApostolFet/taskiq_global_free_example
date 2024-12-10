from typing import AsyncIterator
from dishka import Provider, Scope, provide
from taskiq import AsyncBroker
from taskiq_aio_pika import AioPikaBroker
from taskiq_redis import RedisAsyncResultBackend

from my_app.adapters import OneStrategy, TaskIQDoTask
from my_app.interfaces import DoTask, Strategy

class MyProvider(Provider):

    strategy = provide(OneStrategy, provides=Strategy, scope=Scope.REQUEST)


class DoTaskProvider(Provider):
    scope = Scope.APP

    do_task = provide(TaskIQDoTask, provides=DoTask)

    @provide
    async def create_broker(self) -> AsyncIterator[AsyncBroker]:
        result_backend = RedisAsyncResultBackend("redis://redis:6379/0")
        broker = AioPikaBroker(
            "amqp://guest:guest@rabbit:5672",
        ).with_result_backend(result_backend)

        await broker.startup()
        try:
            yield broker
        finally:
            await broker.shutdown()


