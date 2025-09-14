from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    # This tells Pydantic to load settings from a .env file
    model_config = SettingsConfigDict(env_file=".env")

    DATABASE_URL: str

# Create a single instance of the settings to be used throughout the app
settings = Settings()