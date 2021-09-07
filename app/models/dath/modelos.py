from datetime import date
from dateutil.relativedelta import relativedelta
import enum
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.dialects.postgresql.base import TIMESTAMP
from sqlalchemy.sql.expression import null
from sqlalchemy import Column, ForeignKey, text, func
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import Date, Enum, Integer, String
from app.models import Base
from app.models.core.modelos_principales import Etnia, Nacionalidad

""""
    Autor: Ing. Gabriel Acuña
    Descripción: Este módulo contiene los modelos concernientes a profesores y funcionarios 
    pertenecientes a la institución
"""

class TipoIdentificacion(enum.Enum):
    CEDULA = "CEDULA"
    PASAPORTE = "PASAPORTE"

class Sexo(enum.Enum):
    HOMBRE = "HOMBRE"
    MUJER = "MUJER"


class InformacionPersonal(Base):
    ''' Este modelo contiene la infromación personal de profesores y funcionarios 
    pertenecientes a la institucion'''

    __tablename__ = "datos_personales"
    tipo_identificacion = Column(Enum(TipoIdentificacion), nullable=False)
    identificacion = Column(String(10), nullable=False, primary_key=True)
    primer_nombre = Column(String(30), nullable=False)
    segundo_nombre = Column(String(30), nullable=False)
    primer_apellido = Column(String(30), nullable=False)
    segundo_apellido = Column(String(30), nullable=False)
    sexo = Column(Enum(Sexo), nullable=False)
    fecha_nacimiento = Column(Date, nullable=False)
    id_pais_origen = Column(ForeignKey("paises.id"))
    id_estado_civil = Column(ForeignKey("estados_civiles.id"))
    id_discapacidad = Column(ForeignKey("discapacidades.id"), nullable=False)
    carnet_conadis = Column(String(13), default='', nullable=False)
    porcentaje_discapacidad = Column(Integer, default=0)
    id_etnia = Column(ForeignKey("etnias.id"))
    id_nacionalidad = Column(ForeignKey("nacionalidades.id"), nullable=False,default='')
    correo_institucional = Column(String(80), nullable=False, unique=True)
    correo_personal = Column(String, nullable=False, unique=True)
    telefono_domicilio = Column(String(10), default="0000000000", nullable=False)
    telefono_movil = Column(String(13), nullable=False)
    direccion_domicilio = relationship('Direccion')
    etnia = relationship('Etnia')
    nacionalidad = relationship('Nacionalidad')
    tipo_sangre = Column(String(5), nullable=False)
    lencencia_coduccion = Column(String(2), nullable=False, default='')

    def calcular_edad(self):
        hoy = date.today()
        print(hoy, self.fecha_nacimiento)
        edad = relativedelta(hoy, self.fecha_nacimiento)
    
        return {
            "años": edad.years,
            "meses": edad.months,
            "dias": edad.days
        }


class DireccionDomicilio(Base):
    __tablename__ = "direcciones_domiciliarias"
    id = Column(UUID, primary_key=True, index=True, server_default=text("uuid_generate_v4()"))
    id_persona = Column(ForeignKey('datos_personales.identificacion'), nullable=False)
    id_provincia = Column(ForeignKey("provincias.id"), nullable=False)
    id_canton = Column(ForeignKey("cantones.id"), nullable=False)
    id_parroquia = Column(String(40))
    calle1 = Column(String(30), nullable=False)
    calle2 = Column(String(30))
    

class ExpedienteLaboral(Base):
    __tablename__ = "expedientes_laborales"
    id = Column(UUID, primary_key=True, index=True, server_default=text("uuid_generate_v4()"))
    id_persona = Column(ForeignKey('datos_presonales.identificacion'), nullable=False)
    registrado_en = Column(TIMESTAMP, server_default=func.now())
    actualizado_en = Column(TIMESTAMP, server_default=func.now(),
                            onupdate=func.current_timestamp())

class TipoPersonal(enum.Enum):
    FUNCIONARIIO = "FUNCIONARIO"
    PROFESOR = "PROFESOR"

class DetalleExpedianteLaboral(Base):
    __tablename__ = "detalles_expedientes_laborales"
    id = Column(UUID, primary_key=True, index=True, server_default=text("uuid_generate_v4()"))
    id_historial = Column(ForeignKey())
    tipo_porsonal = Column(Enum(TipoPersonal))
    id_tipo_documento = Column(ForeignKey('tipos_documento'))
    motivo_accion = Column(String(30), default='')
    numero_documento = Column(String(30), nullable=False)
    contrato_relacionado = Column(String(30), nullable=False, default='')
    ingreso_concurso = Column(String(2), nullable=False)
    id_relacion_ies = Column(ForeignKey('relaciones_ies.id'), nullable=False)
    id_tipo_escalafon = Column(ForeignKey)
    

    
