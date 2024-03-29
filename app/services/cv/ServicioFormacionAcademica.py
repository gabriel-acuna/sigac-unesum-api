from typing import List

from sqlalchemy.sql.expression import select
from app.schemas.cv.FormacionAcademicaSchema import *
from app.models.cv.modelos import FormacionAcademica,EstadoFormacion as EF
from app.models.core.modelos_principales import Pais, NivelEducativo, Grado, CampoEducativoEspecifico
from app.models.core.modelos_principales import TipoBeca, FinanciamientoBeca, IESNacional
from app.database.conf import AsyncDatabaseSession
import logging


class ServicioFormacionAcademica():

    @classmethod
    async def listar(cls, id_persona: str) -> List[FormacionAcademicaSchema]:
        estudios: List[FormacionAcademicaSchema] = []
        try:
            async_db_session = AsyncDatabaseSession()
            await async_db_session.init()

            results = await async_db_session.execute(
                select(FormacionAcademica).where(
                    FormacionAcademica.id_persona == id_persona
                )
            )
            filas = results.all()
            if filas:
                for fila in filas:
                    pais_or: PaisSchema = None
                    nivel: NivelEducativoSchema = None
                    ies: IESNacionalSchema = None
                    grado: GradoSchema = None
                    campo_estudio: CampoEducativoEspecifico = None
                    beca: TipoBecaSchema = None
                    tipo_financiamiento: FinanciamientoBecaSchema = None

                    estudio: FormacionAcademica
                    estudio = fila[0]

                    result = await async_db_session.execute(
                        select(Pais).where(Pais.id == estudio.id_pais_estudio)
                    )
                    pais = result.scalar_one()
                    pais_or = PaisSchema(**pais.__dict__)
                    result = await async_db_session.execute(
                        select(NivelEducativo).where(
                            NivelEducativo.id == estudio.id_nivel)
                    )
                    nivel_educativo = result.scalar_one()
                    nivel = NivelEducativoSchema(**nivel_educativo.__dict__)
                    if estudio.id_ies:
                        result = await async_db_session.execute(
                            select(IESNacional).where(
                                IESNacional.id == estudio.id_ies
                            )
                        )
                        ies_nacional = result.scalar_one()
                        ies = IESNacionalSchema(
                            **ies_nacional.__dict__
                        )
                    if estudio.id_grado:
                        result = await async_db_session.execute(
                            select(Grado).where(
                                Grado.id == estudio.id_grado
                            )
                        )
                        gr = result.scalar_one()
                        grado = GradoSchema(**gr.__dict__)

                    result = await async_db_session.execute(
                        select(CampoEducativoEspecifico).where(
                            CampoEducativoEspecifico.id == estudio.id_campo_especifico

                        )
                    )
                    campo: CampoEducativoEspecifico = result.scalar_one()
                    campo_estudio = CampoEducativoEspecificoSchema(
                        id=campo.id,
                        campo_amplio=campo.id_campo_amplio,
                        codigo=campo.codigo,
                        descripcion=campo.descripcion
                    )
                    if estudio.id_tipo_beca:
                        result = await async_db_session.execute(
                            select(TipoBeca).where(
                                TipoBeca.id == estudio.id_tipo_beca)
                        )
                        t_beca = result.scalar_one()
                        beca = TipoBecaSchema(**t_beca.__dict__)

                    if estudio.id_financiamiento:
                        result = await async_db_session.execute(
                            select(FinanciamientoBeca).where(
                                FinanciamientoBeca.id == estudio.id_financiamiento)
                        )
                        t_fin = result.scalar_one()
                        
                        tipo_financiamiento = FinanciamientoBecaSchema(
                            **t_fin.__dict__)
                    estado_formacion: EstadoFormacion = EstadoFormacion.CURSANDO
                    if estudio.estado.value == EstadoFormacion.TERMINADA.value:
                        estado_formacion = EstadoFormacion.TERMINADA
                    estudios.append(
                        FormacionAcademicaSchema(
                            id=estudio.id,
                            id_persona=estudio.id_persona,
                            pais_estudio=pais_or,
                            ies=ies,
                            nombre_ies =estudio.nombre_ies,
                            nivel_educativo=nivel,
                            grado=grado,
                            nombre_titulo=estudio.nombre_titulo,
                            campo_especifico=campo_estudio,
                            estado=estado_formacion,
                            fecha_inicio=estudio.fecha_inicio,
                            fecha_fin=estudio.fecha_fin,
                            registro_senescyt=estudio.registro_senescyt,
                            fecha_obtencion_titulo=estudio.fecha_obtencion_titulo,
                            lugar=estudio.lugar,
                            posee_beca=estudio.posee_beca,
                            tipo_beca=beca,
                            monto_beca=estudio.monto_beca,
                            financiamiento=tipo_financiamiento,
                            descripcion=estudio.descripcion

                        )
                    )

        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)
        finally:
            await async_db_session.close()
        return estudios

    @classmethod
    async def buscar_por_id(cls, id: str) -> FormacionAcademicaSchema:
        pais_or: PaisSchema = None
        nivel: NivelEducativoSchema = None
        ies: IESNacionalSchema = None
        grado: GradoSchema = None
        campo_estudio: CampoEducativoEspecifico = None
        beca: TipoBecaSchema = None
        tipo_financiamiento: FinanciamientoBecaSchema = None
        formacion: FormacionAcademicaSchema = None

        try:
            async_db_session = AsyncDatabaseSession()
            await async_db_session.init()
            result = await async_db_session.execute(
                select(FormacionAcademica).where(
                    FormacionAcademica.id == id
                )
            )
           
            respuesta = result.all()
            if respuesta:
                estudio: FormacionAcademica = respuesta[0][0]
                result = await async_db_session.execute(
                    select(Pais).where(Pais.id == estudio.id_pais_estudio)
                )
                pais = result.scalar_one()
                pais_or = PaisSchema(**pais.__dict__)
                result = await async_db_session.execute(
                    select(NivelEducativo).where(
                        NivelEducativo.id == estudio.id_nivel)
                )
                nivel_educativo = result.scalar_one()
                nivel = NivelEducativoSchema(**nivel_educativo.__dict__)
                if estudio.id_ies:
                    result = await async_db_session.execute(
                        select(IESNacional).where(
                            IESNacional.id == estudio.id_ies
                        )
                    )
                    ies_nacional = result.scalar_one()
                    ies = IESNacionalSchema(
                        **ies_nacional.__dict__
                    )
                if estudio.id_grado:
                    result = await async_db_session.execute(
                        select(Grado).where(
                            Grado.id == estudio.id_grado
                        )
                    )
                    gr = result.scalar_one()
                    grado = GradoSchema(**gr.__dict__)

                result = await async_db_session.execute(
                    select(CampoEducativoEspecifico).where(
                        CampoEducativoEspecifico.id == estudio.id_campo_especifico

                    )
                )
                campo = result.scalar_one()
                campo_estudio = CampoEducativoEspecificoSchema(
                    id=campo.id,
                    campo_amplio=campo.id_campo_amplio,
                    codigo=campo.codigo,
                    descripcion=campo.descripcion)
                if estudio.id_tipo_beca:
                    result = await async_db_session.execute(
                        select(TipoBeca).where(
                            TipoBeca.id == estudio.id_tipo_beca)
                    )
                    t_beca = result.scalar_one()
                    beca = TipoBecaSchema(**t_beca.__dict__)
                if estudio.id_tipo_beca:
                    result = await async_db_session.execute(
                        select(TipoBeca).where(
                            TipoBeca.id == estudio.id_tipo_beca)
                    )
                    t_beca = result.scalar_one()
                    beca = TipoBecaSchema(**t_beca.__dict__)
                if estudio.id_financiamiento:
                    result = await async_db_session.execute(
                        select(FinanciamientoBeca).where(
                            FinanciamientoBeca.id == estudio.id_financiamiento)
                    )
                    t_fin = result.scalar_one()
                    tipo_financiamiento = FinanciamientoBecaSchema(
                        **t_fin.__dict__)
                estado_formacion: EstadoFormacion = EstadoFormacion.CURSANDO
                if estudio.estado.value == EstadoFormacion.TERMINADA.value:
                    estado_formacion = EstadoFormacion.TERMINADA
                formacion = FormacionAcademicaSchema(
                    id=estudio.id,
                    id_persona=estudio.id_persona,
                    pais_estudio=pais_or,
                    ies=ies,
                    nombre_ies =estudio.nombre_ies,
                    nivel_educativo=nivel,
                    grado=grado,
                    nombre_titulo=estudio.nombre_titulo,
                    campo_especifico=campo_estudio,
                    estado=estado_formacion,
                    fecha_inicio=estudio.fecha_inicio,
                    fecha_fin=estudio.fecha_fin,
                    registro_senescyt=estudio.registro_senescyt,
                    fecha_obtencion_titulo=estudio.fecha_obtencion_titulo,
                    lugar=estudio.lugar,
                    posee_beca=estudio.posee_beca,
                    tipo_beca=beca,
                    monto_beca=estudio.monto_beca,
                    financiamiento=tipo_financiamiento,
                    descripcion=estudio.descripcion

                )
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)
        finally:
            await async_db_session.close()
        return formacion

    @classmethod
    async def agregar_registro(cls, estudio: FormacionAcademicaPostSchema) -> bool:
        estado_formacion: EF = EF.CURSANDO
        if estudio.estado.value == EF.TERMINADA.value:
            estado_formacion = EF.TERMINADA
        try:
            return await FormacionAcademica.crear(
                id_persona=estudio.id_persona,
                id_pais_estudio=estudio.pais_estudio,
                id_ies=estudio.ies,
                nombre_ies=estudio.nombre_ies,
                id_nivel=estudio.nivel_educativo,
                id_grado=estudio.grado,
                nombre_titulo=estudio.nombre_titulo,
                id_campo_especifico=estudio.campo_especifico,
                estado=estado_formacion,
                fecha_inicio=estudio.fecha_inicio,
                fecha_fin=estudio.fecha_fin,
                registro_senescyt=estudio.registro_senescyt,
                fecha_obtencion_titulo=estudio.fecha_obtencion_titulo,
                lugar=estudio.lugar,
                posee_beca=estudio.posee_beca,
                id_tipo_beca=estudio.tipo_beca,
                monto_beca=estudio.monto_beca,
                id_financiamiento=estudio.financiamiento,
                descripcion=estudio.descripcion)
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)

    @classmethod
    async def actualizar_registro(cls, estudio: FormacionAcademicaPutSchema) -> bool:
        try:
            estado_formacion: EF = EF.CURSANDO
            if estudio.estado.value == EF.TERMINADA.value:
                estado_formacion = EF.TERMINADA

            return await FormacionAcademica.actualizar(
                id=estudio.id,
                id_pais_estudio=estudio.pais_estudio,
                id_ies=estudio.ies,
                nombre_ies=estudio.nombre_ies,
                id_nivel=estudio.nivel_educativo,
                id_grado=estudio.grado,
                nombre_titulo=estudio.nombre_titulo,
                id_campo_especifico=estudio.campo_especifico,
                estado=estado_formacion,
                fecha_inicio=estudio.fecha_inicio,
                fecha_fin=estudio.fecha_fin,
                registro_senescyt=estudio.registro_senescyt,
                fecha_obtencion_titulo=estudio.fecha_obtencion_titulo,
                lugar=estudio.lugar,
                posee_beca=estudio.posee_beca,
                id_tipo_beca=estudio.tipo_beca,
                monto_beca=estudio.monto_beca,
                id_financiamiento=estudio.financiamiento,
                descripcion=estudio.descripcion)
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)

    @classmethod
    async def eliminar_registro(cls, id: str) -> bool:

        try:
            return await FormacionAcademica.eliminar(id)
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)

    @classmethod
    async def existe(cls, estudio: FormacionAcademicaPostSchema) -> bool:
        try:
            async_db_session = AsyncDatabaseSession()
            await async_db_session.init()
            result = await async_db_session.execute(
                select(FormacionAcademica).where(
                    FormacionAcademica.id_nivel == estudio.nivel_educativo,
                    FormacionAcademica.nombre_titulo == estudio.nivel_educativo
                )
            )
            existe = result.all()
            if existe:
                return True
            return False
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)
        finally:
            await async_db_session.close()
