from typing import Optional
from pydantic.networks import EmailStr
from app.schemas.core.EstadoCivilSchema import EstadoCivilSchema
from datetime import date
from app.schemas.core.PaisSchema import PaisSchema
from pydantic import BaseModel, Field
from app.schemas.dath.DireccionSchema import *
from app.schemas.core.DiscapacidadSchema import DiscapacidadSchema
from app.schemas.core.EtniaSchema import EtniaSchema
from app.schemas.core.NacionalidadSchema import NacionalidadSchema
import enum


class TipoIdentificacion(str, enum.Enum):
    CEDULA = "CEDULA"
    PASAPORTE = "PASAPORTE"


class Sexo(str, enum.Enum):
    HOMBRE = "HOMBRE"
    MUJER = "MUJER"


class InformacionPersonalSchema(BaseModel):
    tipo_identificacion: TipoIdentificacion
    identificacion: str
    primer_nombre: str
    segundo_nombre: str
    primer_apellido: str
    segundo_apellido: str
    sexo: Sexo
    fecha_nacimiento: date
    edad: dict
    pais_origen: PaisSchema
    estado_civil: EstadoCivilSchema
    discapacidad: DiscapacidadSchema
    carnet_conadis: str
    porcentaje_discapacidad: int
    etnia: EtniaSchema
    nacionalidad: Optional[NacionalidadSchema]
    correo_institucional: EmailStr
    correo_personal: EmailStr
    telefono_domicilio: Optional[str]
    telefono_movil: str
    direccion_domicilio: DireccionSchema
    tipo_sangre: str
    licencia_conduccion: str
    fecha_ingreso: date

class InformacionPersonalPostSchema(BaseModel):
    tipo_identificacion: TipoIdentificacion
    identificacion: str = Field(...)
    primer_nombre: str = Field(...)
    segundo_nombre: str = Field(...)
    primer_apellido: str = Field(...)
    segundo_apellido: str = Field(...)
    sexo: Sexo
    fecha_nacimiento: date = Field(...)
    pais_origen: int = Field(...)
    estado_civil: int = Field(...)
    discapacidad: str = Field(...)
    carnet_conadis: Optional[str]
    porcentaje_discapacidad: int = Field(...)
    etnia: str = Field(...)
    nacionalidad: Optional[str]
    correo_institucional: EmailStr = Field(...)
    correo_personal: EmailStr = Field(...)
    telefono_domicilio: Optional[str]
    telefono_movil: str = Field(...)
    direccion_domicilio: DireccionPostSchema
    tipo_sangre: str = Field(...)
    licencia_conduccion: Optional[str]
    fecha_ingreso: date


class InformacionPersonalPutSchema(BaseModel):
    tipo_identificacion: TipoIdentificacion
    primer_nombre: str = Field(...)
    segundo_nombre: str = Field(...)
    primer_apellido: str = Field(...)
    segundo_apellido: str = Field(...)
    sexo: Sexo
    fecha_nacimiento: date = Field(...)
    pais_origen: int = Field(...)
    estado_civil: int = Field(...)
    discapacidad: str = Field(...)
    carnet_conadis: Optional[str]
    porcentaje_discapacidad: int = Field(...)
    etnia: str = Field(...)
    nacionalidad: Optional[str]
    correo_institucional: EmailStr = Field(...)
    correo_personal: EmailStr = Field(...)
    telefono_domicilio: Optional[str]
    telefono_movil: str = Field(...)
    direccion_domicilio: DireccionPostSchema
    tipo_sangre: str = Field(...)
    licencia_conduccion: Optional[str]
    fecha_ingreso:date