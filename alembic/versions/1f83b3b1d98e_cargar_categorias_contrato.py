"""cargar categorias contrato

Revision ID: 1f83b3b1d98e
Revises: 6431463cb24f
Create Date: 2021-10-05 21:41:40.718427

"""
from typing import List
from alembic import op
import sqlalchemy as sa
from sqlalchemy.orm.session import Session
from sqlalchemy.sql.expression import delete, select
from app.models.core.modelos_principales import CategoriaContratoProfesor


# revision identifiers, used by Alembic.
revision = '1f83b3b1d98e'
down_revision = '6431463cb24f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    categorias = [
        'TITULAR PRINCIPAL',
        'TITULAR AGREGADO',
        'TITULAR AUXILIAR',
        'HONORARIO',
        'INVITADO',
        'OCASIONAL',
        'OCASIONALII',
        'PRINCIPAL1',
        'PRINCIPAL2',
        'PRINCIPAL3',
        'AGREGADO1',
        'AGREGADO2',
        'AGREGADO3',
        'AUXILIAR1',
        'AUXILIAR2'
        'TITULAR NO ESCALAFONADO'
    ]
    session = Session(bind=op.get_bind())
    lista: List[CategoriaContratoProfesor] = []
    for categoria in categorias:
        results = session.execute(
            select(CategoriaContratoProfesor).where(CategoriaContratoProfesor.categoria_contrato==categoria)
        )
        existe = results.all()
        if existe:
            break
        lista.append(CategoriaContratoProfesor(categoria_contrato=categoria))
        
    
    
    session.add_all(lista)
    session.commit()
        
    session.close()

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    session = Session(bind=op.get_bind())
    session.execute(delete(CategoriaContratoProfesor))
    session.commit()
    session.close()
    # ### end Alembic commands ###