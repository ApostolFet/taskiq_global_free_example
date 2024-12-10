from taskiq import AsyncBroker

from my_app.interfaces import DoTask, Strategy
from my_app.tasks import my_task


class OneStrategy(Strategy):
    async def __call__(self) -> int:
        return 1


class TaskIQDoTask(DoTask):
    def __init__(self, broker: AsyncBroker) -> None:
        self._broker = broker

    async def __call__(self) -> str:
        task = self._broker.task(my_task)
        task = await task.kiq()
        return task.task_id

    async def get_result(self, task_id: str) -> int:
        result = await self._broker.result_backend.get_result(task_id)
        return result.return_value
