from typing import List
from app.schemas.dath.DeclaracionPatrimonialSchema import *
from app.schemas.dath.InformacionPersonalSchema import InformacionPersonalBasicaSchema
from app.models.dath.modelos import DeclaracionPatrimonial, InformacionPersonal
from app.database.conf import AsyncDatabaseSession
from sqlalchemy.sql.expression import select
import logging


class ServicioDeclaracionPatrimonial():

    @classmethod
    async def listar(cls) -> List[DeclaracionPatrimonialDetalladaSchema]:
        declaraciones: List[DeclaracionPatrimonialDetalladaSchema] = []
        try:
            filas = await DeclaracionPatrimonial.listar()
            if filas:
                async_db_session = AsyncDatabaseSession()
                await async_db_session.init()
                for fila in filas:
                    declaracion: DeclaracionPatrimonial = fila[0]
                    result = await async_db_session.execute(
                        select(InformacionPersonal.identificacion, InformacionPersonal.primer_nombre, InformacionPersonal.segundo_nombre,
                               InformacionPersonal.primer_apellido, InformacionPersonal.segundo_apellido
                               ).where(InformacionPersonal.identificacion == declaracion.id_persona)

                    )
                    persona = result.all()
                    declaraciones.append(
                        DeclaracionPatrimonialDetalladaSchema(
                            id=declaracion.id,
                            persona=InformacionPersonalBasicaSchema(
                                tipo_identificacion=persona[0][0],
                                identificacion=persona[0][1],
                                primer_nombre=persona[0][2],
                                segundo_nombre=persona[0][3],
                                primer_apellido=persona[0][4],
                                segundo_apellido=persona[0][5],
                            ),
                            tipo_declaracion=declaracion.tipo_declaracion,
                            fecha_presentacion=declaracion.fecha_presentacion
                        )
                    )
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)
        finally:
            await async_db_session.close()
        return declaraciones

    @classmethod
    async def listar_por_id_persona(cls, id_persona: str) -> List[DeclaracionPatrimonialSchema]:
        declaraciones: List[DeclaracionPatrimonialSchema] = []
        try:
            filas = await DeclaracionPatrimonial.filtarPor(id_persona=id_persona)
            for fila in filas:
                declaraciones.append(
                    DeclaracionPatrimonialSchema(**fila[0].__dict__))
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)
        return declaraciones

    @classmethod
    async def buscar_por_id(cls, id: str) -> DeclaracionPatrimonialSchema:
        declaracion: DeclaracionPatrimonialSchema = None
        try:
            respuesta = await DeclaracionPatrimonial.obtener(id)
            if respuesta:
                declaracion = DeclaracionPatrimonialSchema(
                    respuesta[0].__dict__)
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)
        return declaracion

    @classmethod
    async def agregar_registro(cls, declaracion: DeclaracionPatrimonialPostSchema) -> bool:
        try:
            return await DeclaracionPatrimonial.crear(
                id_persona=declaracion.persona,
                tipo_declaracion=declaracion.tipo_declaracion,
                fech_presentacion=declaracion.fecha_presentacion
            )
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)

    @classmethod
    async def actualizar_registro(cls, declaracion: DeclaracionPatrimonialPutSchema) -> bool:
        try:
            return await DeclaracionPatrimonial.crear(
                id=declaracion.id,
                tipo_declaracion=declaracion.tipo_declaracion,
                fech_presentacion=declaracion.fecha_presentacion
            )
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)

    @classmethod
    async def eliminar_registro(cls) -> bool:
        try:
            return DeclaracionPatrimonial.eliminar(id)
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)

    @classmethod
    async def existe(cls, declaracion: DeclaracionPatrimonialPostSchema) -> bool:
        try:
            existe = await DeclaracionPatrimonial.filtarPor(
                id_persona=declaracion.persona,
                tipo_declaracion=declaracion.tipo_declaracion,
                fecha_presentacion=declaracion.fecha_presentacion
            )
            return True if existe else False
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)