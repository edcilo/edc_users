from ms.tasks.worker import celery
from ms.repositories.userRepository import UserRepository


@celery.task(name="update_cache")
def update_cache():
    userRepo = UserRepository()
    userRepo.updateCache()
