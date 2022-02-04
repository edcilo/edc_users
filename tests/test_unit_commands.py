from fixture import app, runner
from ms.commands import createadmin
from ms.models import User


def test_createadmin(app, runner):
    with app.app_context():
        result = runner.invoke(createadmin, [
            '--email', 'notanemail',
            '--phone', '1231231231',
            '--password', 'secret'])
        assert 'This field must be a valid email address' in result.output

        result = runner.invoke(createadmin, [
            '--email', 'test@example.com',
            '--phone', '123',
            '--password', 'secret'])
        assert 'This field is not valid' in result.output

        result = runner.invoke(createadmin, [
            '--email', 'test@example.com',
            '--phone', '1231231231',
            '--password', 'pass'])
        assert 'This field is not valid' in result.output

        result = runner.invoke(createadmin, [
            '--email', 'test@example.com',
            '--phone', '1231231231',
            '--password', 'secret'])
        assert 'The user was created successfully' in result.output

        user = User.query.filter_by(email='test@example.com').first()
        assert user is not None
        assert user.email == 'test@example.com'
        assert user.phone == '1231231231'
        assert user.password is not None
