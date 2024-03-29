from sqlalchemy.dialects.postgresql.base import TIMESTAMP
from sqlalchemy.sql.expression import select
from sqlalchemy.sql.schema import ForeignKey, Table
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import Boolean, DateTime, Enum
from app.models import Base
from sqlalchemy import Column, String, func, text
from sqlalchemy.dialects.postgresql import UUID
from app.models.async_crud import OperacionesEscrituraAsinconas, EliminacionAsincrona, OperacionesLecturaAsincronas
import enum
import bcrypt

""" 
    Autor: Ing. Gabriel Acuña
    Descripción: Este módulo contiene los modelos encargados de la gestión de cuentas de usuario y roles
"""

rol_usuario = Table(
    'roles_usuarios',
    Base.metadata,
    Column('rol_id', ForeignKey('roles.id')),
    Column('usuario_id', ForeignKey('cuentas_usuarios.id'))

)


class Rol(Base, OperacionesEscrituraAsinconas,
          OperacionesLecturaAsincronas, EliminacionAsincrona):
    __tablename__ = "roles"
    id = Column(UUID, primary_key=True, index=True, server_default=text("uuid_generate_v4()"))
    rol = Column(String(50), nullable=False)
    descripcion = Column(String(120), nullable=False)
    registrado_en = Column(TIMESTAMP, server_default=func.now())
    actualizado_en = Column(
        TIMESTAMP, server_default=func.now(),    onupdate=func.current_timestamp())
    usuarios = relationship("CuentaUsuario", secondary=rol_usuario)


class CuentaUsuario(Base, OperacionesEscrituraAsinconas,
                    OperacionesLecturaAsincronas, EliminacionAsincrona):
    __tablename__ = "cuentas_usuarios"
    id = Column(UUID, primary_key=True, index=True, server_default=text("uuid_generate_v4()"))
    primer_nombre = Column(String(30), nullable=False)
    segundo_nombre = Column(String(30), nullable=False)
    primer_apellido = Column(String(30), nullable=False)
    segundo_apellido = Column(String(30), nullable=False)
    email = Column(String(80), nullable=False, unique=True)
    clave_encriptada = Column(String(), nullable=False)
    estado = Column(Boolean, default=True)
    registrado_en = Column(TIMESTAMP, server_default=func.now())
    actualizado_en = Column(
        TIMESTAMP, server_default=func.now(),    onupdate=func.current_timestamp())
    roles = relationship("Rol", secondary=rol_usuario, overlaps="usuarios")

    @classmethod
    def cifrar_clave(cls, clave):
        password = bcrypt.hashpw(clave.encode(), bcrypt.gensalt())
        return password.decode('utf-8')


class TipoToken(enum.Enum):
    acceso = "Access Token"
    solicitud_cambio_calve = "Resset Password Token Request"


class TokenAutorizacion(Base, OperacionesEscrituraAsinconas,
                        OperacionesLecturaAsincronas):
    __tablename__ = "tokens_autorizaciones"
    id = Column(UUID, primary_key=True, index=True, server_default=text("uuid_generate_v4()"))
    tipo_token = Column(Enum(TipoToken), nullable=False)
    token = Column(String(), nullable=False)
    usuario_id = Column(ForeignKey("cuentas_usuarios.id"))
    generado_en = Column(TIMESTAMP, server_default=func.now())
    usado_hasta = Column(DateTime, nullable=True)
    estado = Column(Boolean(), default=True)
