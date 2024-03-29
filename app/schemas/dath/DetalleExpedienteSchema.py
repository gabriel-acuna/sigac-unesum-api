from datetime import date
from typing import Optional
from pydantic import BaseModel, Field, validator
import enum
from app.schemas.core.TipoDocumentoSchema import TipoDocumentoSchema
from app.schemas.core.RelacionIESSchema import RelacionIESSchema
from app.schemas.core.TipoEscalafonNombramientoSchema import TipoEscalafonNombramientoSchema
from app.schemas.core.CategoriaContratoProfesorSchema import CategoriaContratoProfesorSchema
from app.schemas.core.TiempoDedicacionProfesorSchema import TiempoDedicacionProfesorSchema
from app.schemas.core.TipoFuncionarioSchema import TipoFuncionarioSchema
from app.schemas.core.AreaInstitucionalSchema import AreaInstitucionSchema
from app.schemas.core.TipoDocenteLOESSchema import TipoDocenteLOESSchema
from app.schemas.core.CategoriaDocenteLOSEPSchema import CategoriaDocenteLOSEPSchema
from app.schemas.core.NivelEducativoSchema import NivelEducativoSchema
from app.schemas.dath.TipoContratoSchema import TipoContratoSchema
from app.schemas.dath.TipoNombramientoSchema import TipoNombramientoSchema


class TipoPersonal(str, enum.Enum):
    FUNCIONARIO = "FUNCIONARIO"
    PROFESOR = "PROFESOR"


class Opciones(str, enum.Enum):
    SI = "SI"
    NO = "NO"


class DetalleExpedienteSchema(BaseModel):
    id: str
    id_expediente: str
    tipo_personal: TipoPersonal
    tipo_documento: TipoDocumentoSchema
    motivo_accion: Optional[str]
    tipo_contrato: Optional[TipoContratoSchema]
    tipo_nombramiento: Optional[TipoNombramientoSchema]
    descripcion: Optional[str]
    numero_documento: str
    contrato_relacionado: Optional[str]
    ingreso_concurso: Opciones
    relacion_ies: RelacionIESSchema
    escalafon_nombramiento: Optional[TipoEscalafonNombramientoSchema]
    categoria_contrato: Optional[CategoriaContratoProfesorSchema]
    tiempo_dedicacion: Optional[TiempoDedicacionProfesorSchema]
    remuneracion_mensual: float
    remuneracion_hora: Optional[float]
    fecha_inicio: date
    fecha_fin: Optional[date]
    tipo_funcionario: Optional[TipoFuncionarioSchema]
    cargo: Optional[str]
    tipo_docente: Optional[TipoDocenteLOESSchema]
    categoria_docente: Optional[CategoriaDocenteLOSEPSchema]
    puesto_jerarquico: Optional[Opciones]
    horas_laborables_semanales: Optional[int]
    area: AreaInstitucionSchema
    sub_area: Optional[AreaInstitucionSchema]
    nivel: Optional[NivelEducativoSchema]


class DetalleExpedienteFuncionarioPostSchema(BaseModel):
    tipo_personal: TipoPersonal
    tipo_documento: str = Field(...)
    tipo_contrato: Optional[str] = Field()
    tipo_nombramiento: Optional[str] = Field()
    motivo_accion: Optional[str] = Field()
    descripcion: Optional[str] = Field()
    numero_documento: str = Field(...)
    relacion_ies: str = Field(...)
    fecha_inicio: date = Field(...)
    fecha_fin: Optional[date] = Field()
    ingreso_concurso: Opciones = Field(...)
    remuneracion_mensual: float = Field(...)
    tipo_funcionario: str = Field(...)
    cargo: str = Field(...)
    tipo_docente: str = Field(...)
    categoria_docente: str = Field(...)
    puesto_jerarquico: Opciones = Field(...)
    horas_laborables_semanales: int = Field(...)
    area: int = Field(...)
    sub_area: Optional[int] = Field()

    @validator("fecha_inicio")
    def fecha_ingreso_validaciones(cls, value):
        hoy = date.today()
        if value > hoy:
            raise ValueError(
                "La fecha de ingreso no puede ser mayor a la fecha actual")
        return value


class DetalleExpedienteFuncionarioPutSchema(BaseModel):
    id: str = Field(...)
    tipo_personal: TipoPersonal
    tipo_documento: str = Field(...)
    tipo_contrato: Optional[str] = Field()
    tipo_nombramiento: Optional[str] = Field()
    motivo_accion: Optional[str] = Field()
    descripcion: Optional[str] = Field()
    numero_documento: str = Field(...)
    relacion_ies: str = Field(...)
    fecha_inicio: date = Field(...)
    fecha_fin: Optional[date] = Field()
    ingreso_concurso: Opciones = Field(...)
    remuneracion_mensual: float = Field(...)
    tipo_funcionario: str = Field(...)
    cargo: str = Field(...)
    tipo_docente: str = Field(...)
    categoria_docente: str = Field(...)
    puesto_jerarquico: Opciones = Field(...)
    horas_laborables_semanales: int = Field(...)
    area: int = Field(...)
    sub_area: Optional[int] = Field()


class DetalleExpedienteProfesorPostSchema(BaseModel):
    tipo_personal: TipoPersonal
    tipo_documento: str = Field(...)
    tipo_contrato: Optional[str] = Field()
    tipo_nombramiento: Optional[str] = Field()
    motivo_accion: Optional[str] = Field()
    descripcion: Optional[str] = Field()
    numero_documento: str = Field(...)
    contrato_relacionado: Optional[str] = Field()
    ingreso_concurso: Opciones
    relacion_ies: str = Field(...)
    escalafon_nombramiento: Optional[str]
    categoria_contrato: Optional[str]
    tiempo_dedicacion: Optional[str]
    remuneracion_mensual: float = Field(...)
    remuneracion_hora: Optional[float] = Field()
    fecha_inicio: date = Field(...)
    fecha_fin: Optional[date] = Field()
    area: int = Field(...)
    sub_area: Optional[int] = Field()
    nivel: str = Field(...)


class DetalleExpedienteProfesorPutSchema(BaseModel):
    id: str = Field(...)
    tipo_personal: TipoPersonal
    tipo_documento: str = Field(...)
    tipo_contrato: Optional[str] = Field()
    tipo_nombramiento: Optional[str] = Field()
    motivo_accion: Optional[str] = Field()
    numero_documento: str = Field(...)
    descripcion: Optional[str] = Field()
    contrato_relacionado: Optional[str] = Field()
    ingreso_concurso: Opciones
    relacion_ies: str = Field(...)
    escalafon_nombramiento: str = Field(...)
    categoria_contrato: str = Field(...)
    tiempo_dedicacion: str = Field(...)
    remuneracion_mensual: float = Field(...)
    remuneracion_hora: Optional[float] = Field()
    fecha_inicio: date = Field(...)
    fecha_fin: Optional[date] = Field()
    area: int = Field(...)
    sub_area: Optional[int] = Field()
    nivel: str = Field(...)
