from pydantic import BaseSettings
from sqlalchemy.ext.declarative import declarative_base

class Settings(BaseSettings):
    API_V1_STR: str = '/api/v1'
    DB_URL: str = "postgres://api_curso_ns4h_user:UA3bS6mmLT9O1y0WZCGAxgYqlWnytgyA@dpg-ckfjt5uct0pc73bnhvkg-a.ohio-postgres.render.com/api_curso_ns4h"
    DBBaseModel = declarative_base()

    class Config:
        case_sensitive = True

Settings = Settings()