
from datetime import datetime
from app.schemas.validaciones import longitud_maxima
from pydantic import BaseModel, Field, validator


class CategoriaContratoProfesorSchema(BaseModel):
    id: str
    categoria_contrato: str
    registrado_en: datetime
    actualizado_en: datetime


class CategoriaContratoProfesorPostSchema(BaseModel):
    categoria_contrato: str = Field(...)

    @validator("categoria_contrato")
    def categoria_contrato_maxima_longitud(cls, value):
        return longitud_maxima(50, value,8)

    class Config:
        eschema_extra = {
            "example": {
                "categoria": "TITULAR PRINCIPAL"
            }
        }


class CategoriaContratoProfesorPutSchema(BaseModel):
    id: str = Field(...)
    categoria_contrato: str = Field(..., max_length=50)

    @validator("categoria_contrato")
    def categoria_contrato_maxima_longitud(cls, value):
        return longitud_maxima(50, value, 8)
