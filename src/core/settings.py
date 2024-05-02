from pydantic_settings import BaseSettings


class ServiceSettings(BaseSettings):

    project_name: str = "Biblus"
    project_port: int = 228


settings = ServiceSettings()
