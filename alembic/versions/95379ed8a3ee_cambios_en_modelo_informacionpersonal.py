"""cambios en modelo InformacionPersonal

Revision ID: 95379ed8a3ee
Revises: 361677108e35
Create Date: 2021-09-18 17:57:03.232067

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '95379ed8a3ee'
down_revision = '361677108e35'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('datos_personales', 'id_nacionalidad',
               existing_type=postgresql.UUID(),
               nullable=True)
    op.alter_column('datos_personales', 'telefono_domicilio',
               existing_type=sa.VARCHAR(length=10),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('datos_personales', 'telefono_domicilio',
               existing_type=sa.VARCHAR(length=10),
               nullable=False)
    op.alter_column('datos_personales', 'id_nacionalidad',
               existing_type=postgresql.UUID(),
               nullable=False)
    # ### end Alembic commands ###
