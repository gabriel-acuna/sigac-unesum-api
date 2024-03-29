"""correcion en nombre de columna

Revision ID: ea676797411f
Revises: af0f4d8a44a3
Create Date: 2021-10-05 11:51:15.660163

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ea676797411f'
down_revision = 'af0f4d8a44a3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('referencias', sa.Column('apellidos', sa.String(length=80), nullable=False))
    op.drop_column('referencias', 'apelidos')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('referencias', sa.Column('apelidos', sa.VARCHAR(length=80), autoincrement=False, nullable=False))
    op.drop_column('referencias', 'apellidos')
    # ### end Alembic commands ###
