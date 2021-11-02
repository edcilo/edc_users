from ms.repositories import userRepo
from ms.helpers.jwt import jwtHelper



def createUser(data):
    return userRepo.add(data)

def createJhonDoe():
    return createUser({
        'username': 'JhonDoe',
        'password': 'secret',
        'email': 'jhon.doe@example.com'
    })

def createJWT():
    return jwtHelper.get_tokens({})
