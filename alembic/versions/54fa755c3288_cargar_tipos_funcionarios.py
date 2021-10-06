"""cargar tipos funcionarios

Revision ID: 54fa755c3288
Revises: bbfd8b9b5235
Create Date: 2021-10-05 22:11:32.379833

"""
from alembic import op
import sqlalchemy as sa
from typing import List
from app.models.core.modelos_principales import TipoFuncionario
from sqlalchemy.orm.session import Session
from sqlalchemy.sql.expression import delete, select


# revision identifiers, used by Alembic.
revision = '54fa755c3288'
down_revision = 'bbfd8b9b5235'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    funcionarios = [
        'ADMINISTRATIVO',
        'TRABAJADOR',
        'DIRECTIVO',
        'DOCENTE LOES'
    ]

    session = Session(bind=op.get_bind())
    lista: List[TipoFuncionario] = []
    for funcionario in funcionarios:
        
        results = session.execute(
            select(TipoFuncionario).where(TipoFuncionario.tipo==funcionario)
        )
        existe = results.all()
        if existe:
            break
        lista.append(TipoFuncionario(tipo=funcionario))
        
    
    session.add_all(lista)
    session.commit()
        
    session.close()

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    session = Session(bind=op.get_bind())
    session.execute(delete(TipoFuncionario))
    session.commit()
    session.close()
    # ### end Alembic commands ###
