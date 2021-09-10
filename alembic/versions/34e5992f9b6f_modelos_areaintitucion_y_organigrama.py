"""modelos AreaIntitucion y Organigrama

Revision ID: 34e5992f9b6f
Revises: 78e43689947d
Create Date: 2021-09-10 15:34:41.176334

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '34e5992f9b6f'
down_revision = '78e43689947d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('areas_institucionales',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=80), nullable=False),
    sa.Column('codigo', sa.String(length=30), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('organigrama',
    sa.Column('id_estructura_institucional', sa.Integer(), nullable=False),
    sa.Column('id_area_institucional', sa.Integer(), nullable=False),
    sa.Column('id_sub_area', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['id_area_institucional'], ['areas_institucionales.id'], ),
    sa.ForeignKeyConstraint(['id_estructura_institucional'], ['estructura_organica_institucional.id'], ),
    sa.ForeignKeyConstraint(['id_sub_area'], ['areas_institucionales.id'], ),
    sa.PrimaryKeyConstraint('id_estructura_institucional', 'id_area_institucional')
    )
    op.add_column('estructura_organica_institucional', sa.Column('documento_aprobacion', sa.String(length=80), nullable=False))
    op.add_column('estructura_organica_institucional', sa.Column('fecha_aprobacion', sa.Date(), nullable=False))
    op.drop_column('estructura_organica_institucional', 'id_area')
    op.drop_column('estructura_organica_institucional', 'nombre')
    op.drop_column('estructura_organica_institucional', 'codigo')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('estructura_organica_institucional', sa.Column('codigo', sa.VARCHAR(length=50), autoincrement=False, nullable=True))
    op.add_column('estructura_organica_institucional', sa.Column('nombre', sa.VARCHAR(length=80), autoincrement=False, nullable=False))
    op.add_column('estructura_organica_institucional', sa.Column('id_area', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_column('estructura_organica_institucional', 'fecha_aprobacion')
    op.drop_column('estructura_organica_institucional', 'documento_aprobacion')
    op.drop_table('organigrama')
    op.drop_table('areas_institucionales')
    # ### end Alembic commands ###
