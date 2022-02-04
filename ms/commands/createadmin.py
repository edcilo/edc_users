import click
from flask.cli import with_appcontext
from flaskFormRequest.validators import (
    Email,
    Max,
    Min,
    Regex,
    Unique,
    ValidationError
)
from ms.helpers.regex import phone_regex, password_regex
from ms.models import User
from ms.repositories import UserRepository, RoleRepository


def validateEmail(ctx, param, value):
    emailRule = Email()
    maxRule = Max(250)
    uniqueRule = Unique(User, 'email')

    try:
        emailRule(value, 'email', {}, [])
        maxRule(value, 'email', {}, [])
        uniqueRule(value, 'email', {}, [])
        return value
    except ValidationError as err:
        raise click.BadParameter(str(err))


def validatePhone(ctx, param, value):
    minRule = Min(9)
    maxRule = Max(15)
    uniqueRule = Unique(User, 'phone')
    try:
        minRule(value, 'phone', {}, [])
        maxRule(value, 'phone', {}, [])
        uniqueRule(value, 'phone', {}, [])
        return value
    except ValidationError as err:
        raise click.BadParameter(str(err))


def validatePassword(ctx, param, value):
    minRule = Min(6)
    maxRule = Max(255)
    try:
        minRule(value, 'password', {}, [])
        maxRule(value, 'password', {}, [])
        return value
    except ValidationError as err:
        raise click.BadParameter(str(err))


@click.command(name='createadmin',
               help='Create a new admin user.')
@click.option('--email',
              prompt='E-mail',
              required=True,
              callback=validateEmail)
@click.option('--phone', prompt='Phone', required=True, callback=validatePhone)
@click.password_option(callback=validatePassword)
@with_appcontext
def createadmin(email, phone, password):
    role_repo = RoleRepository()
    admin_role = role_repo.find_by_attr('name', 'admin')
    user_repo = UserRepository()
    user_repo.add({
        "email": email,
        "phone": phone,
        "password": password,
        "role_id": admin_role.id
    })
    print('The user was created successfully')
