"""modelos para la gestión de CV

Revision ID: dff6a42542b2
Revises: 4985cbc5b9ad
Create Date: 2021-09-21 22:07:54.429248

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'dff6a42542b2'
down_revision = '4985cbc5b9ad'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Grados',
    sa.Column('id', postgresql.UUID(), server_default=sa.text('uuid_generate_v4()'), nullable=False),
    sa.Column('grado', sa.String(length=80), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_Grados_id'), 'Grados', ['id'], unique=False)
    op.create_table('finaciamiento_beca',
    sa.Column('id', postgresql.UUID(), server_default=sa.text('uuid_generate_v4()'), nullable=False),
    sa.Column('financiamiento', sa.String(length=30), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_finaciamiento_beca_id'), 'finaciamiento_beca', ['id'], unique=False)
    op.create_table('tipo_beca',
    sa.Column('id', postgresql.UUID(), server_default=sa.text('uuid_generate_v4()'), nullable=False),
    sa.Column('tipo_beca', sa.String(length=30), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_tipo_beca_id'), 'tipo_beca', ['id'], unique=False)
    op.create_table('capacitaciones',
    sa.Column('id', postgresql.UUID(), server_default=sa.text('uuid_generate_v4()'), nullable=False),
    sa.Column('id_persona', sa.String(length=10), nullable=False),
    sa.Column('tipo_evento', sa.String(length=30), nullable=False),
    sa.Column('institucion_organizadora', sa.String(length=80), nullable=False),
    sa.Column('lugar', sa.String(length=30), nullable=False),
    sa.Column('horas', sa.Integer(), nullable=False),
    sa.Column('inicio', sa.Date(), nullable=False),
    sa.Column('fin', sa.Date(), nullable=False),
    sa.Column('tipo_certificado', sa.Enum('ASISTENCIA', 'APROBACION', name='tipoCertificado'), nullable=True),
    sa.Column('url_certificado', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['id_persona'], ['datos_personales.identificacion'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_capacitaciones_id'), 'capacitaciones', ['id'], unique=False)
    op.create_table('referencias',
    sa.Column('id', postgresql.UUID(), server_default=sa.text('uuid_generate_v4()'), nullable=False),
    sa.Column('id_persona', sa.String(length=10), nullable=False),
    sa.Column('referencia', sa.Enum('PERSONAL', 'LABORAL', name='tipoReferencia'), nullable=True),
    sa.Column('apelidos', sa.String(length=80), nullable=False),
    sa.Column('nombres', sa.String(length=80), nullable=False),
    sa.Column('direccion', sa.String(length=120), nullable=False),
    sa.Column('correo_electronico', sa.String(length=80), nullable=True),
    sa.Column('telefono_domicilio', sa.String(length=10), nullable=True),
    sa.Column('telefono_movil', sa.String(length=13), nullable=False),
    sa.ForeignKeyConstraint(['id_persona'], ['datos_personales.identificacion'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_referencias_id'), 'referencias', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_referencias_id'), table_name='referencias')
    op.drop_table('referencias')
    op.drop_index(op.f('ix_capacitaciones_id'), table_name='capacitaciones')
    op.drop_table('capacitaciones')
    op.drop_index(op.f('ix_tipo_beca_id'), table_name='tipo_beca')
    op.drop_table('tipo_beca')
    op.drop_index(op.f('ix_finaciamiento_beca_id'), table_name='finaciamiento_beca')
    op.drop_table('finaciamiento_beca')
    op.drop_index(op.f('ix_Grados_id'), table_name='Grados')
    op.drop_table('Grados')
    sa.Enum(name='tipoReferencia').drop(op.get_bind(), checkfirst=False)
    sa.Enum(name='tipoCertificado').drop(op.get_bind(), checkfirst=False)
    # ### end Alembic commands ###
