from flaskFormRequest import FormRequest
from flaskFormRequest.validators import (
    File,
    Nullable,
    MimeTypes
)

class ClientUpdloaFilesForm(FormRequest):
    def rules(self):
        image_types = ('image/png', 'image/jpeg', 'image/gif',)

        rules = {
            Nullable(),
            File(),
            MimeTypes(image_types)
        }

        return {
            "legal_id_front": rules,
            "legal_id_back": rules,
            "proof_of_address": rules,
        }
