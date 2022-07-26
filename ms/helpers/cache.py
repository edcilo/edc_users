from ms import app
from ms.repositories import UserRepository, AppRepository


def update_cache():
    userRepo = UserRepository()
    appRepo = AppRepository()

    prefix = "ms-users-"
    users = userRepo.all()
    apps = appRepo.all()

    app.cache.truncate(prefix)

    for u in users:
        userRepo.setCache(u)
    for a in apps:
        appRepo.setCache(a)
