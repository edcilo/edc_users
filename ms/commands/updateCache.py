import click
import os
from flask.cli import with_appcontext
from ms.helpers import cache


@click.command(name='updateCache',
               help='Update permissions cache')
@with_appcontext
def updatecache():
    cache.update_cache()
    click.echo('Cache updated')
