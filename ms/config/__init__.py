from dotenv import load_dotenv
from ms import app
from .appConfig import app_config
from .cacheConfig import cache_config
from .dbConfig import db_config
from .storageConfig import storage_config


load_dotenv()


app.config.update(**app_config)
app.config.update(**cache_config)
app.config.update(**db_config)
app.config.update(**storage_config)
