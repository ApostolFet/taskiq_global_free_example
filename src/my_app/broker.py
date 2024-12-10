
from dishka import make_async_container
from taskiq_aio_pika import AioPikaBroker
from taskiq_redis import RedisAsyncResultBackend

from dishka.integrations.taskiq import setup_dishka
from my_app.providers import MyProvider
from my_app.tasks import register_tasks


result_backend = RedisAsyncResultBackend("redis://redis:6379/0")
broker = AioPikaBroker(
    "amqp://guest:guest@rabbit:5672",
).with_result_backend(result_backend)

register_tasks(broker)

container = make_async_container(MyProvider())
setup_dishka(container, broker)
