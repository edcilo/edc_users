import click
import os
from flask.cli import with_appcontext
from ms.repositories import UserRepository
from ms.repositories import AppRepository


@click.command(name='updateCache',
               help='Update permissions cache')
@with_appcontext
def updatecache():
    userRepo = UserRepository()
    appRepo = AppRepository()

    userRepo.updateCache()
    appRepo.updateCache()
