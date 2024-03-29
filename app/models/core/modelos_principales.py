from sqlalchemy.dialects.postgresql.base import TIMESTAMP
from sqlalchemy.sql.schema import ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import DATE, Date, Integer
from app.models import Base
from sqlalchemy import Column, String, func, text
from sqlalchemy.dialects.postgresql import UUID
from app.models.async_crud import OperacionesLecturaAsincronas, OperacionesEscrituraAsinconas, EliminacionAsincrona

""" 
    Autor: Ing. Gabriel Acuña
    Descripción: Este módulo contiene los modelos asociados a los INSTRUCTIVO CARGA MASIVA SISTEMA
    DE INFORMACIÓN INTEGRAL DE LA EDUCACIÓN SUPERIOR Versión 6
"""


class Discapacidad(Base, OperacionesEscrituraAsinconas,
                   OperacionesLecturaAsincronas, EliminacionAsincrona):
    __tablename__ = "discapacidades"
    id = Column(UUID, primary_key=True, index=True,
                server_default=text("uuid_generate_v4()"))
    discapacidad = Column(String(30), unique=True, nullable=False)
    registrado_en = Column(TIMESTAMP, server_default=func.now())
    actualizado_en = Column(TIMESTAMP, server_default=func.now(),
                            onupdate=func.current_timestamp())


class Etnia(Base, OperacionesEscrituraAsinconas,
            OperacionesLecturaAsincronas, EliminacionAsincrona):
    __tablename__ = "etnias"
    id = Column(UUID, primary_key=True, index=True,
                server_default=text("uuid_generate_v4()"))
    etnia = Column(String(50), nullable=False, unique=True)
    registrado_en = Column(TIMESTAMP, server_default=func.now())
    actualizado_en = Column(TIMESTAMP, server_default=func.now(),
                            onupdate=func.current_timestamp())


class Nacionalidad(Base, OperacionesEscrituraAsinconas,
                   OperacionesLecturaAsincronas, EliminacionAsincrona):
    __tablename__ = "nacionalidades"
    id = Column(UUID, primary_key=True, index=True,
                server_default=text("uuid_generate_v4()"))
    nacionalidad = Column(String(50), nullable=False, unique=True)
    registrado_en = Column(TIMESTAMP, server_default=func.now())
    actualizado_en = Column(TIMESTAMP, server_default=func.now(),
                            onupdate=func.current_timestamp())


class TipoDocumento(Base, OperacionesEscrituraAsinconas,
                    OperacionesLecturaAsincronas, EliminacionAsincrona):
    __tablename__ = "tipos_documento"
    id = Column(UUID, primary_key=True, index=True,
                server_default=text("uuid_generate_v4()"))
    tipo_documento = Column(String(50), nullable=False, unique=True)
    registrado_en = Column(TIMESTAMP, server_default=func.now())
    actualizado_en = Column(TIMESTAMP, server_default=func.now(),
                            onupdate=func.current_timestamp())


class RelacionIES(Base, OperacionesEscrituraAsinconas,
                  OperacionesLecturaAsincronas, EliminacionAsincrona):
    __tablename__ = "relaciones_ies"
    id = Column(UUID, primary_key=True, index=True,
                server_default=text("uuid_generate_v4()"))
    relacion = Column(String(50), nullable=False, unique=True)
    registrado_en = Column(TIMESTAMP, server_default=func.now())
    actualizado_en = Column(TIMESTAMP, server_default=func.now(),
                            onupdate=func.current_timestamp())


class TipoEscalafonNombramiento(Base, OperacionesEscrituraAsinconas,
                                OperacionesLecturaAsincronas, EliminacionAsincrona):
    __tablename__ = "tipos_escalafones_nombramientos"
    id = Column(UUID, primary_key=True, index=True,
                server_default=text("uuid_generate_v4()"))
    escalafon_nombramiento = Column(String(50), nullable=False, unique=True)
    registrado_en = Column(TIMESTAMP, server_default=func.now())
    actualizado_en = Column(TIMESTAMP, server_default=func.now(),
                            onupdate=func.current_timestamp())


class CategoriaContratoProfesor(Base, OperacionesEscrituraAsinconas,
                                OperacionesLecturaAsincronas, EliminacionAsincrona):
    __tablename__ = "categorias_contratos_profesores"
    id = Column(UUID, primary_key=True, index=True,
                server_default=text("uuid_generate_v4()"))
    categoria_contrato = Column(String(50), nullable=False, unique=True)
    registrado_en = Column(TIMESTAMP, server_default=func.now())
    actualizado_en = Column(TIMESTAMP, server_default=func.now(),
                            onupdate=func.current_timestamp())


class TiempoDedicacionProfesor(Base, OperacionesEscrituraAsinconas,
                               OperacionesLecturaAsincronas, EliminacionAsincrona):
    __tablename__ = "tiempo_dedicacion_profesores"
    id = Column(UUID, primary_key=True, index=True,
                server_default=text("uuid_generate_v4()"))
    tiempo_dedicacion = Column(String(50), nullable=False, unique=True)
    registrado_en = Column(TIMESTAMP, server_default=func.now())
    actualizado_en = Column(TIMESTAMP, server_default=func.now(),
                            onupdate=func.current_timestamp())


class NivelEducativo(Base, OperacionesEscrituraAsinconas,
                     OperacionesLecturaAsincronas, EliminacionAsincrona):
    __tablename__ = "nivel_educativo"
    id = Column(UUID, primary_key=True, index=True,
                server_default=text("uuid_generate_v4()"))
    nivel = Column(String(50), nullable=False, unique=True)
    registrado_en = Column(TIMESTAMP, server_default=func.now())
    actualizado_en = Column(TIMESTAMP, server_default=func.now(),
                            onupdate=func.current_timestamp())


class TipoFuncionario(Base, OperacionesEscrituraAsinconas,
                      OperacionesLecturaAsincronas, EliminacionAsincrona):
    __tablename__ = "tipo_funcionarios"
    id = Column(UUID, primary_key=True, index=True,
                server_default=text("uuid_generate_v4()"))
    tipo = Column(String(50), nullable=False, unique=True)
    registrado_en = Column(TIMESTAMP, server_default=func.now())
    actualizado_en = Column(TIMESTAMP, server_default=func.now(),
                            onupdate=func.current_timestamp())


class TipoDocenteLOES(Base, OperacionesEscrituraAsinconas,
                      OperacionesLecturaAsincronas, EliminacionAsincrona):
    __tablename__ = "tipos_docente_loes"
    id = Column(UUID, primary_key=True, index=True,
                server_default=text("uuid_generate_v4()"))
    tipo_docente = Column(String(50), nullable=False, unique=True)
    registrado_en = Column(TIMESTAMP, server_default=func.now())
    actualizado_en = Column(
        TIMESTAMP, server_default=func.now(),    onupdate=func.current_timestamp())


class CategoriaDocenteLOSEP(Base, OperacionesEscrituraAsinconas,
                            OperacionesLecturaAsincronas, EliminacionAsincrona):
    __tablename__ = "categorias_docentes_losep"
    id = Column(UUID, primary_key=True, index=True,
                server_default=text("uuid_generate_v4()"))
    categoria_docente = Column(String(50), unique=True, nullable=False)
    registrado_en = Column(TIMESTAMP, server_default=func.now())
    actualizado_en = Column(
        TIMESTAMP, server_default=func.now(),    onupdate=func.current_timestamp())


class Pais(Base, OperacionesEscrituraAsinconas,
           OperacionesLecturaAsincronas, EliminacionAsincrona):
    __tablename__ = "paises"
    __table_args__ = (
        UniqueConstraint('pais', name='uc_pais'),
    )
    id = Column(Integer, primary_key=True, index=True)
    pais = Column(String(120), nullable=False)
    nacionalidad = Column(String(120), nullable=True, default='')
    registrado_en = Column(TIMESTAMP, server_default=func.now())
    actualizado_en = Column(
        TIMESTAMP, server_default=func.now(),    onupdate=func.current_timestamp())


class Provincia(Base, OperacionesEscrituraAsinconas,
                OperacionesLecturaAsincronas, EliminacionAsincrona):
    __tablename__ = "provincias"
    __table_args__ = (
        UniqueConstraint('provincia', name='uc_provincia'),
    )

    id = Column(Integer, primary_key=True, index=True)
    provincia = Column(String(120), nullable=False)
    cantones = relationship("Canton")
    registrado_en = Column(TIMESTAMP, server_default=func.now())
    actualizado_en = Column(
        TIMESTAMP, server_default=func.now(),    onupdate=func.current_timestamp())


class Canton(Base, OperacionesEscrituraAsinconas,
             OperacionesLecturaAsincronas, EliminacionAsincrona):
    __tablename__ = "cantones"
    __table_args__ = (
        UniqueConstraint('canton', 'provincia_id', name='uc_canton_provincia'),
    )
    id = Column(Integer, primary_key=True)
    canton = Column(String(120), nullable=False)
    provincia_id = Column(Integer, ForeignKey("provincias.id"))
    registrado_en = Column(TIMESTAMP, server_default=func.now())
    actualizado_en = Column(
        TIMESTAMP, server_default=func.now(),    onupdate=func.current_timestamp())


class EstadoCivil(Base, OperacionesEscrituraAsinconas, OperacionesLecturaAsincronas, EliminacionAsincrona):
    __tablename__ = "estados_civiles"
    id = Column(Integer, primary_key=True)
    estado_civil = Column(String(30), nullable=False)


class EstructuraInstitucional(Base, OperacionesEscrituraAsinconas, OperacionesLecturaAsincronas, EliminacionAsincrona):
    __tablename__ = "estructura_organica_institucional"
    id = Column(Integer, primary_key=True)
    documento_aprobacion = Column(String(80), nullable=False)
    fecha_aprobacion = Column(Date, nullable=False)

class AreaInstitucion(Base,OperacionesLecturaAsincronas, OperacionesEscrituraAsinconas, EliminacionAsincrona):
    __tablename__ = "areas_institucionales"
    id = Column(Integer, primary_key=True)
    nombre = Column(String(80), nullable=False)
    codigo = Column(String(30), default='')

class Organigrama(Base, OperacionesEscrituraAsinconas, OperacionesLecturaAsincronas, EliminacionAsincrona):
    __tablename__ ="organigrama"
    id_estructura_institucional = Column(Integer, ForeignKey('estructura_organica_institucional.id'), primary_key=True)
    id_area_institucional = Column(Integer, ForeignKey('areas_institucionales.id'), primary_key=True)
    id_sub_area = Column(Integer, ForeignKey('areas_institucionales.id'), default=0, primary_key=True)

class Grado(Base, OperacionesEscrituraAsinconas,
    OperacionesLecturaAsincronas, EliminacionAsincrona):
    __tablename__ = "grados"
    id = Column(UUID, primary_key=True, index=True,
                server_default=text("uuid_generate_v4()"))
    grado = Column(String(80), nullable=False)

class TipoBeca(Base,OperacionesEscrituraAsinconas,
    OperacionesLecturaAsincronas, EliminacionAsincrona):
    __tablename__ = "tipo_beca"
    id = Column(UUID, primary_key=True, index=True,
                server_default=text("uuid_generate_v4()"))
    tipo_beca = Column(String(30), nullable=False)

class FinanciamientoBeca(Base, OperacionesEscrituraAsinconas,
    OperacionesLecturaAsincronas, EliminacionAsincrona):
    __tablename__ = "financiamiento_beca"
    id = Column(UUID, primary_key=True, index=True,
                server_default=text("uuid_generate_v4()"))
    financiamiento = Column(String(30), nullable=False)

class CampoEducativoAmplio(Base, OperacionesEscrituraAsinconas,
    OperacionesLecturaAsincronas, EliminacionAsincrona):
    __tablename__ = "campo_educativo_amplio"
    id = Column(UUID, primary_key=True, index=True,
                server_default=text("uuid_generate_v4()"))
    codigo = Column(String(8), nullable=False)
    descripcion = Column(String(120), nullable=False)
    campos_especificos = relationship('CampoEducativoEspecifico', cascade='save-update')
    
class CampoEducativoEspecifico(Base, OperacionesEscrituraAsinconas,
    OperacionesLecturaAsincronas, EliminacionAsincrona):
    __tablename__ = "campo_educativo_especifico"
    id = Column(UUID, primary_key=True, index=True,
                server_default=text("uuid_generate_v4()"))
    id_campo_amplio = Column(ForeignKey('campo_educativo_amplio.id'), nullable=False)
    codigo = Column(String(8), nullable=False)
    descripcion = Column(String(120), nullable=False)
    campos_detallados = relationship('CampoEducativoDetallado', cascade='save-update')

class CampoEducativoDetallado(Base,
    OperacionesEscrituraAsinconas,
    OperacionesLecturaAsincronas,
    EliminacionAsincrona):
    __tablename__ = "campo_educativo_detallado"
    id = Column(UUID, primary_key=True, index=True,
                server_default=text("uuid_generate_v4()"))
    id_campo_especifico = Column(ForeignKey('campo_educativo_especifico.id'), nullable=False)
    codigo = Column(String(8), nullable=False)
    descripcion = Column(String(120), nullable=False)

class IESNacional(Base, OperacionesLecturaAsincronas,
    OperacionesEscrituraAsinconas, EliminacionAsincrona):
    __tablename__ = "ies_nacionales"
    id = Column(UUID, primary_key=True, index=True,
                server_default=text("uuid_generate_v4()"))
    codigo = Column(String(4), nullable=False)
    institucion = Column(String(130), nullable=False)

