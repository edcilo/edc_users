from dotenv import load_dotenv
from ms import app
from ms.config.appConfig import app_config
from ms.config.dbConfig import db_config


load_dotenv()


app.config.update(**app_config)
app.config.update(**db_config)
