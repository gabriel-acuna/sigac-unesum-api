"""cambios en modelo capacitacion

Revision ID: 13f1892aebb7
Revises: 131994d1e88b
Create Date: 2021-11-28 18:00:19.899993

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '13f1892aebb7'
down_revision = '131994d1e88b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tipos_eventos',
    sa.Column('id', postgresql.UUID(), server_default=sa.text('uuid_generate_v4()'), nullable=False),
    sa.Column('evento', sa.String(length=120), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_tipos_eventos_id'), 'tipos_eventos', ['id'], unique=False)
    op.add_column('capacitaciones', sa.Column('funcion_evento', sa.String(length=75), nullable=True))
    op.add_column('capacitaciones', sa.Column('id_pais', sa.Integer(), nullable=True))
    op.create_foreign_key('capacitaciones_id_paises_fk', 'capacitaciones', 'paises', ['id_pais'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('capacitaciones_id_paises_fk', 'capacitaciones', type_='foreignkey')
    op.drop_column('capacitaciones', 'id_pais')
    op.drop_column('capacitaciones', 'funcion_evento')
    op.drop_index(op.f('ix_tipos_eventos_id'), table_name='tipos_eventos')
    op.drop_table('tipos_eventos')
    # ### end Alembic commands ###
