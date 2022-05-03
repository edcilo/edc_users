from celery import Celery
from ms import app


redisConfig = app.config.get("REDIS", dict())
redisHost = redisConfig.get("HOST")
redisPost = redisConfig.get("PORT")
redisDB = redisConfig.get("DATABASE")


celery = Celery('worker')
celery.conf.broker_url = f'redis://{redisHost}:{redisPost}/1'
celery.conf.result_backend = f'redis://{redisHost}:{redisPost}/2'
celery.conf.imports = ['ms.tasks', 'ms.tasks.updateCache', ]
