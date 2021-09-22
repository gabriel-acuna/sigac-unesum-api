"""cambios en detalle expediente laboral

Revision ID: 4985cbc5b9ad
Revises: 95379ed8a3ee
Create Date: 2021-09-21 20:10:58.101810

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '4985cbc5b9ad'
down_revision = '95379ed8a3ee'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('detalles_expedientes_laborales', 'id_expediente',
               existing_type=postgresql.UUID(),
               nullable=False)
    op.alter_column('detalles_expedientes_laborales', 'tipo_personal',
               existing_type=postgresql.ENUM('FUNCIONARIIO', 'PROFESOR', name='tipoPersonal'),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('detalles_expedientes_laborales', 'tipo_personal',
               existing_type=postgresql.ENUM('FUNCIONARIIO', 'PROFESOR', name='tipoPersonal'),
               nullable=True)
    op.alter_column('detalles_expedientes_laborales', 'id_expediente',
               existing_type=postgresql.UUID(),
               nullable=True)
    # ### end Alembic commands ###