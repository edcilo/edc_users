from ms import app
from ms.commands.autopep8 import pep8
from ms.commands.createadmin import createadmin


app.cli.add_command(pep8)
app.cli.add_command(createadmin)
