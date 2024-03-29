from app.schemas.core.DiscapacidadSchema import DiscapacidadPostSchema
from app.models.core.modelos_principales import Discapacidad, EstadoCivil, Etnia
from datetime import date
from app.schemas.dath.InformacionPersonalSchema import InformacionPersonalPostSchema, Sexo, TipoIdentificacion, InformacionPersonalSchema
from app.schemas.dath.DireccionSchema import DireccionPostSchema
from app.services.core.ServicioDiscapacidad import ServicioDiscapacidad
from app.services.core.ServicioEstadoCivil import ServicioEstadoCivil
from app.services.core.ServicioEtnia import ServicioEtnia
from app.services.dath.ServicioInformacionPersonal import *
import pytest
from app.schemas.dath import *
from decouple import config


@pytest.mark.asyncio
async def test_agregar_registro():

    direccion = DireccionPostSchema(
        id_provincia=12,
        id_canton=139,
        parroquia='SAN LORENZO',
        calle1='CHIMBORAZO',
        calle2='FEBRES COREDERO',
        referencia='S/N'
    )

    estado_civil_existe = await ServicioEstadoCivil.existe(EstadoCivil(estado_civil='SOLTERO/A'))
    if not estado_civil_existe:
        await ServicioEstadoCivil.agregar_registro(EstadoCivil(estado_civil='SOLTERO/A'))
    estado_civil = await EstadoCivil.filtarPor(estado_civil='SOLTERO/A')

    discapacidad = Discapacidad(discapacidad='NINGUNA')
    existe = await ServicioDiscapacidad.existe(discapacidad)
    if not existe:
        await ServicioDiscapacidad.agregar_registro(discapacidad)
    d = await Discapacidad.filtarPor(discapacidad='NINGUNA')

    existe_etnia = await ServicioEtnia.existe(Etnia(etnia='MONTUBIO/A'))
    if not existe_etnia:
        await ServicioEtnia.agregar_registro(Etnia(etnia='MONTUBIO/A'))
    etnia = await Etnia.filtarPor(etnia='MONTUBIO/A')

    # parametro para el método agregar_registro
    data = InformacionPersonalPostSchema(
        tipo_identificacion=TipoIdentificacion.CEDULA,
        identificacion=1314056407,
        primer_nombre='Gabriel',
        segundo_nombre='Stefano',
        primer_apellido='Acuña',
        segundo_apellido='Regalado',
        sexo=Sexo.HOMBRE,
        fecha_nacimiento=date(1993, 9, 27),
        pais_origen=68,
        estado_civil=estado_civil[0][0].id,
        discapacidad=d[0][0].id,
        porcentaje_discapacidad=0,
        etnia=etnia[0][0].id,
        correo_institucional=config('ADMIN_EMAIL'),
        correo_personal=config('EMAIL'),
        telefono_movil='+593985910098',
        direccion_domicilio=direccion,
        tipo_sangre='O+',
        fecha_ingreso= date(2018,8,15)

    )
    params = {'id': data.identificacion,
              'correo_institucional': data.correo_institucional}
    persona_existe = await ServicioInformacionPersonal.existe(**params
                                                              )
    # elimina el registro en caso que exista para evitar que falle el test
    if persona_existe:
        await ServicioInformacionPersonal.eliminar_registro(
            id=data.identificacion
        )
    registrado = await ServicioInformacionPersonal.agregar_registro(persona=data)
    assert registrado == True


@pytest.mark.asyncio
async def test_actualizar_registro():

    direccion = DireccionPostSchema(
        id_provincia=12,
        id_canton=139,
        parroquia='SAN LORENZO',
        calle1='CHIMBORAZO',
        calle2='FEBRES CORDERO',
        referencia='S/N'
    )

    estado_civil_existe = await ServicioEstadoCivil.existe(EstadoCivil(estado_civil='SOLTERO/A'))
    if not estado_civil_existe:
        await ServicioEstadoCivil.agregar_registro(EstadoCivil(estado_civil='SOLTERO/A'))
    estado_civil = await EstadoCivil.filtarPor(estado_civil='SOLTERO/A')

    discapacidad = Discapacidad(discapacidad='NINGUNA')
    existe = await ServicioDiscapacidad.existe(discapacidad)
    if not existe:
        await ServicioDiscapacidad.agregar_registro(discapacidad)
    d = await Discapacidad.filtarPor(discapacidad='NINGUNA')

    existe_etnia = await ServicioEtnia.existe(Etnia(etnia='MONTUBIO/A'))
    if not existe_etnia:
        await ServicioEtnia.agregar_registro(Etnia(etnia='MONTUBIO/A'))
    etnia = await Etnia.filtarPor(etnia='MONTUBIO/A')

    # parametro para el método actualizar_registro
    data = InformacionPersonalPutSchema(
        tipo_identificacion=TipoIdentificacion.CEDULA,
        primer_nombre='Gabriel',
        segundo_nombre='Stefano',
        primer_apellido='Acuña',
        segundo_apellido='Regalado',
        sexo=Sexo.HOMBRE,
        fecha_nacimiento=date(1993, 9, 27),
        pais_origen=68,
        estado_civil=estado_civil[0][0].id,
        discapacidad=d[0][0].id,
        porcentaje_discapacidad=0,
        etnia=etnia[0][0].id,
        correo_institucional=config('ADMIN_EMAIL'),
        correo_personal=config('EMAIL'),
        telefono_movil='+593985910098',
        direccion_domicilio=direccion,
        tipo_sangre='O+',
        fecha_ingreso= date(2018,8,15)

    )
    actualizado = await ServicioInformacionPersonal.actualizar_registro(persona=data, id='1314056407')
    assert actualizado == True


@pytest.mark.asyncio
async def test_buscar_por_id():
    persona = await ServicioInformacionPersonal.buscar_por_id(id='1314056407')
    assert persona is not None
    assert persona.direccion_domicilio.calle2 == 'FEBRES CORDERO'

@pytest.mark.asyncio
async def test_listar():
    personas = await ServicioInformacionPersonal.listar()
    assert len(personas) > 0
    print(personas[0].edad)
    
