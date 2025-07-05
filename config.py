from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    mongodb_host: str
    mongodb_user: str
    mongodb_password: str

    gigachat_key: str

    model_config = SettingsConfigDict(env_file='.env')

    def get_mongo_uri(self):
        user = self.mongodb_user
        password = self.mongodb_password
        host = self.mongodb_host
        return f'mongodb://{user}:{password}@{host}:27017'

settings = Settings()