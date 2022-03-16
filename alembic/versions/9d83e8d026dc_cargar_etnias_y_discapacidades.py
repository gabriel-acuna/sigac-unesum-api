"""cargar etnias y discapacidades

Revision ID: 9d83e8d026dc
Revises: 6e795c658b58
Create Date: 2022-03-16 17:57:09.543894

"""
from alembic import op
import sqlalchemy as sa
from typing import List
from sqlalchemy.orm.session import Session
from app.models.core.modelos_principales import Discapacidad, Etnia
from sqlalchemy.sql.expression import delete, select


# revision identifiers, used by Alembic.
revision = '9d83e8d026dc'
down_revision = '6e795c658b58'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    listado_discapacidades: List[str] = ['AUDITIVA',
                                         'FISICA MOTORA',
                                         'INTELECTUAL',
                                         'LENGUAJE',
                                         'MENTAL PSICOSOCIAL',
                                         'VISUAL',
                                         'NINGUNA']

    session = Session(bind=op.get_bind())
    lista: List[Discapacidad] = []
    for discapacidad in listado_discapacidades:
        results = session.execute(
            select(Discapacidad).where(
                Discapacidad.discapacidad == discapacidad)
        )
        existe = results.all()
        if existe:
            break
        lista.append(Discapacidad(discapacidad=discapacidad))

    session.add_all(lista)
    session.commit()

    listado_etnias: List[str] = [
        'INDIGENA',
        'AFROECUATORIANO/A',
        'NEGRO/A',
        'MULATO/A',
        'MONTUBIO/A',
        'MESTIZO/A',
        'BLANCO/A',
        'OTRO',
        'NO REGISTRA'
    ]

    lista_etinas: List[Discapacidad] = []
    for etnia in listado_etnias:
        results = session.execute(
            select(Etnia).where(
                Etnia.etnia == etnia)
        )
        existe = results.all()
        if existe:
            break
        lista_etinas.append(Etnia(etnia=etnia))

    session.add_all(lista_etinas)
    session.commit()

    session.close()
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    session = Session(bind=op.get_bind())
    session.execute(delete(Discapacidad))
    session.execute(delete(Etnia))
    session.commit()
    session.close()
    # ### end Alembic commands ###
