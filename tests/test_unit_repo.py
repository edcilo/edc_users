from fixture import client
from helpers import createJhonDoe, getRole
from ms.models import User, Role
from ms.repositories import UserRepository, RoleRepository
from ms.db import db


def test_user_repo(client):
    userRepo = UserRepository()

    model = userRepo.get_model()
    assert model == User

    role = Role.query.filter_by(name='client').first()

    # TEST: add new user
    user = userRepo.add({
        'username': 'jhon.doe',
        'email': 'jhon.doe@example.com',
        'phone': '1231231231',
        'password': 'secret',
        'role_id': role.id, })
    assert isinstance(user, User)
    assert user.id is not None
    assert user.password is not None

    # TEST: activate and deactivate
    assert user.is_active == False
    user = userRepo.activate(user.id, fail=True)
    assert user.is_active == True
    user = userRepo.deactivate(user.id, fail=True)
    assert user.is_active == False

    # TEST: find user by id
    user_found = userRepo.find(user.id)
    assert isinstance(user_found, User)
    user_not_found = userRepo.find('foo')
    assert user_not_found is None

    # TEST: find user by attribute
    user_found = userRepo.find_by_attr('phone', '1231231231')
    assert isinstance(user_found, User)
    userRepo.soft_delete(user_found.id)
    user_found = userRepo.find_by_attr('phone', '1231231231', with_deleted=True)
    assert user_found is not None
    userRepo.restore(user_found.id)

    # TEST: find optional
    user_found = userRepo.find_optional({
        'phone': '1231231231',
        'email': 'jhon.doe@foo.com'})
    assert isinstance(user_found, User)
    assert user_found.email == 'jhon.doe@example.com'

    # TEST: get all
    users = userRepo.all()
    assert isinstance(users, list)
    assert len(users) == 9
    results = userRepo.all('jhon')
    assert len(results) == 1
    results = userRepo.all('foo')
    assert len(results) == 0

    # TEST: update
    user_updated = userRepo.update(user.id, {'phone': '3213213213'})
    assert user_updated.phone == '3213213213'

    # TEST: update password
    old_password = user.password
    user_updated = userRepo.update_password(user.id, 'secret2')
    assert old_password != user_updated.password
    assert not user.verify_password('secret1')
    assert user.verify_password('secret2')

    # TEST: soft delete
    user = userRepo.soft_delete(user.id)
    assert user.deleted == True

    # TEST: restore
    user = userRepo.restore(user.id)
    assert user.deleted == False

    # TEST: delete
    userRepo.delete(user.id)
    user = userRepo.find(user.id)
    assert user is None
