from pydantic import Field
from pydantic_settings import BaseSettings


class ServiceSettings(BaseSettings):

    app_name: str = "Biblus"
    app_port: int = 1228

    elastic_host: str = Field("elasticsearch", env="ELASTIC_HOST")
    elastic_port: int = Field(5601, env="ELASTIC_PORT")
    elastic_user: str = Field("elastic", env="ELASTIC_USER")
    elastic_password: str = Field("change_me!", env="ELASTIC_PASSWORD")
    elastic_url: str = Field(f"http://{elastic_host}:{elastic_port}")
    books_index: str = Field("book")


settings = ServiceSettings()
