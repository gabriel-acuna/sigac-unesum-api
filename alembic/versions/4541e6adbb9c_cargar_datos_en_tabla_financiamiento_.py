"""cargar datos en tabla financiamiento_beca

Revision ID: 4541e6adbb9c
Revises: d352d6001091
Create Date: 2021-10-20 09:48:47.542249

"""
from typing import List
from alembic import op
import sqlalchemy as sa
from sqlalchemy import orm
from sqlalchemy.dialects import postgresql
from sqlalchemy.orm.session import Session
from sqlalchemy.sql.expression import select, delete

from app.models.core.modelos_principales import FinanciamientoBeca


# revision identifiers, used by Alembic.
revision = '4541e6adbb9c'
down_revision = 'd352d6001091'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('financiamiento_beca',
    sa.Column('id', postgresql.UUID(), server_default=sa.text('uuid_generate_v4()'), nullable=False),
    sa.Column('financiamiento', sa.String(length=30), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    lista: List[FinanciamientoBeca] = []
    financiamientos = [
        'AUTOGESTION',
        'SENESCYT',
        'TRANSFERENCIA ESTADO IES',
        'OTRO'

    ]
    session = Session(bind=op.get_bind())
    
    for item in financiamientos:
        results =session.execute(
            select(FinanciamientoBeca).where(
                FinanciamientoBeca.financiamiento == item
            )
        )
        existe = results.all()
        if existe:
            break
        lista.append(FinanciamientoBeca(financiamiento=item))

    session.add_all(lista)
    session.commit()
    session.close()
    op.create_index(op.f('ix_financiamiento_beca_id'), 'financiamiento_beca', ['id'], unique=False)
    op.drop_index('ix_finaciamiento_beca_id', table_name='finaciamiento_beca')
    op.drop_table('finaciamiento_beca')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('finaciamiento_beca',
    sa.Column('id', postgresql.UUID(), server_default=sa.text('uuid_generate_v4()'), autoincrement=False, nullable=False),
    sa.Column('financiamiento', sa.VARCHAR(length=30), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='finaciamiento_beca_pkey')
    )
    op.create_index('ix_finaciamiento_beca_id', 'finaciamiento_beca', ['id'], unique=False)
    op.drop_index(op.f('ix_financiamiento_beca_id'), table_name='financiamiento_beca')
    op.drop_table('financiamiento_beca')
    # ### end Alembic commands ###
