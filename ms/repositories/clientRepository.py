from ms.helpers.files import generate_client_filename, upload_file
from ms.models import User, Profile
from ms.repositories.userRepository import UserRepository
from ms.repositories.roleRepository import RoleRepository
from .repository import Repository


class ClientRepository(Repository):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.userRepo = UserRepository()
        self.roleRepo = RoleRepository()

    def get_model(self):
        return User

    def add(self, data):
        role = self.roleRepo.find_by_attr("name", self._model._default_role)
        data['role_id'] = role.id
        user = self.userRepo.add(data)
        user.profile = Profile(data)
        self.db_save(user.profile)
        return user

    def update(self, id, data):
        user = id if isinstance(id, User) else self.userRepo.find(id)
        if user.profile:
            user.profile.update(data)
            self.db_save(user)
        else:
            user.profile = Profile(data)
            self.db_save(user.profile)
        return user

    def upload_files(self, id, data):
        user = id if isinstance(id, User) else self.userRepo.find(id)
        fields = ("legal_id_front", "legal_id_back", "proof_of_address")
        fields_url = {}
        for field in fields:
            if field not in data or data.get(field).content_type is None:
                continue
            file = data.get(field)
            filename = generate_client_filename(user, file)
            path = f"/tmp/{filename}"
            ext = path.split(".")[-1]
            destination = f"/shoppers/{user.id}/{field}.{ext}"
            file.save(path)
            url = upload_file(path, destination)
            fields_url[field] = url
        if len(fields_url) > 0:
            self.update(user, fields_url)
