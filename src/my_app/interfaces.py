from typing import Protocol


class Strategy(Protocol):
    async def __call__(self) -> int:
        ...


class DoTask(Protocol):
    async def __call__(self) -> str:
        ...

    async def get_result(self, task_id: str) -> int:
        ...
        
