from pydantic import Field
from pydantic_settings import BaseSettings


class ServiceSettings(BaseSettings):

    app_name: str = "Biblus"
    app_port: int = 8000

    proxy_host: str = "127.0.0.1"
    proxy_port: int = 9050
    chunk_size: int = 1024

    redis_host: str = Field("redis://redis", env="REDIS_HOST")
    redis_port: int = Field(6380, env="REDIS_PORT")
    redis_url: str = Field(f"{redis_host}:{redis_port}")
    cache_expire: int = Field(600)

    elastic_host: str = Field("elasticsearch", env="ELASTIC_HOST")
    elastic_port: int = Field(5601, env="ELASTIC_PORT")
    elastic_user: str = Field("elastic", env="ELASTIC_USER")
    elastic_password: str = Field("change_me!", env="ELASTIC_PASSWORD")
    elastic_url: str = Field(f"http://{elastic_host}:{elastic_port}")
    books_index: str = Field("book")
    book_dwld_option_field: str = "tor_link"


settings = ServiceSettings()
