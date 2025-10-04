from pydantic_settings import BaseSettings, SettingsConfigDict


class Config(BaseSettings):
    hostname: str
    port: int
    database_url: str

    secret_key: str
    algorithm: str
    access_token_expire_minutes: int = 30

    model_config = SettingsConfigDict(env_file=".env")


app_config = Config()
