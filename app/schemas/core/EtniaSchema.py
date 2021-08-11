
from datetime import datetime
from app.schemas.validaciones import longitud_maxima
from pydantic import BaseModel, Field, validator


class EtniaSchema(BaseModel):
    id: str
    etnia: str
    registrado_en: datetime
    actualizado_en: datetime


class EtniaPostSchema(BaseModel):
    etnia: str = Field(...)

    @validator('etnia')
    def etnia_longitud_maxima(cls, value):
        return longitud_maxima(50, value)

    class Config:
        schema_extra = {
            "example": {
                "etnia": "INDIGENA"
            }
        }


class EtniaPutSchema(BaseModel):
    id: str = Field(...)
    etnia: str = Field(...)

    @validator('etnia')
    def etnia_longitud_maxima(cls, value):
        return longitud_maxima(50, value)