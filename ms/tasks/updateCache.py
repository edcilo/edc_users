from ms.tasks.worker import celery
from ms.helpers import cache


@celery.task(name="update_cache")
def update_cache():
    cache.update_cache()
