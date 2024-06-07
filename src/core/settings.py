from pydantic import Field
from pydantic_settings import BaseSettings


class ServiceSettings(BaseSettings):

    app_name: str = "Biblus"
    app_port: int = 8000

    proxy_host: str = "127.0.0.1"
    proxy_port: int = 9050
    chunk_size: int = 1024

    elastic_host: str = Field("elasticsearch", env="ELASTIC_HOST")
    elastic_port: int = Field(5601, env="ELASTIC_PORT")
    elastic_user: str = Field("elastic", env="ELASTIC_USER")
    elastic_password: str = Field("change_me!", env="ELASTIC_PASSWORD")
    elastic_url: str = Field(f"http://{elastic_host}:{elastic_port}")
    books_index: str = Field("book")
    book_dwld_option_field: str = "tor_link"


settings = ServiceSettings()
