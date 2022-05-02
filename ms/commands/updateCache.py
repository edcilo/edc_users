import click
import os
from flask.cli import with_appcontext
from ms.repositories import UserRepository


@click.command(name='updateCache',
               help='Update permissions cache')
@with_appcontext
def updatecache():
    userRepo = UserRepository()
    users = userRepo.all()
    userRepo.cache.truncate()
    for user in users:
        userRepo.setCache(user)
