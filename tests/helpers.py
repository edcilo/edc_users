from ms.repositories import userRepo
from ms.helpers.jwt import jwtHelper



def createUser(data):
    return userRepo.add(data)

def createJhonDoe():
    return createUser({
        'phone': '1231231231',
        'email': 'jhon.doe@example.com',
        'password': 'secret',
    })

def createJWT(payload):
    return jwtHelper.get_tokens(payload)
