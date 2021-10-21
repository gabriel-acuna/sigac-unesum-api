"""nuevos modelos para cv

Revision ID: 68b435498e74
Revises: 27b07307ae73
Create Date: 2021-10-21 15:22:37.559545

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '68b435498e74'
down_revision = '27b07307ae73'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('capacitaciones_facilitadores',
    sa.Column('id', postgresql.UUID(), server_default=sa.text('uuid_generate_v4()'), nullable=False),
    sa.Column('id_persona', sa.String(length=10), nullable=False),
    sa.Column('funcion_evento', sa.String(length=75), nullable=False),
    sa.Column('institucion_organizadora', sa.String(length=80), nullable=False),
    sa.Column('lugar', sa.String(length=120), nullable=False),
    sa.Column('horas', sa.Integer(), nullable=False),
    sa.Column('certificado', sa.String(length=120), nullable=True),
    sa.ForeignKeyConstraint(['id_persona'], ['datos_personales.identificacion'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_capacitaciones_facilitadores_id'), 'capacitaciones_facilitadores', ['id'], unique=False)
    op.create_table('comprension_idiomas',
    sa.Column('id', postgresql.UUID(), server_default=sa.text('uuid_generate_v4()'), nullable=False),
    sa.Column('id_persona', sa.String(length=10), nullable=False),
    sa.Column('idioma', sa.String(length=30), nullable=False),
    sa.Column('lugar_estudio', sa.String(length=120), nullable=False),
    sa.Column('nivel_compresion', sa.Enum('Excelente', 'Buena', 'Limitada', 'Ninguna', name='nivelcompresion'), nullable=False),
    sa.ForeignKeyConstraint(['id_persona'], ['datos_personales.identificacion'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_comprension_idiomas_id'), 'comprension_idiomas', ['id'], unique=False)
    op.create_table('experiencia_laboral_personal',
    sa.Column('id', postgresql.UUID(), server_default=sa.text('uuid_generate_v4()'), nullable=False),
    sa.Column('id_persona', sa.String(length=10), nullable=False),
    sa.Column('empresa', sa.String(length=120), nullable=False),
    sa.Column('lugar', sa.String(length=120), nullable=False),
    sa.Column('cargo', sa.String(length=60), nullable=False),
    sa.Column('inicio', sa.Date(), nullable=False),
    sa.Column('fin', sa.Date(), nullable=True),
    sa.ForeignKeyConstraint(['id_persona'], ['datos_personales.identificacion'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_experiencia_laboral_personal_id'), 'experiencia_laboral_personal', ['id'], unique=False)
    op.create_table('meritos_distinciones',
    sa.Column('id', postgresql.UUID(), server_default=sa.text('uuid_generate_v4()'), nullable=False),
    sa.Column('id_persona', sa.String(length=10), nullable=False),
    sa.Column('titulo', sa.String(length=130), nullable=False),
    sa.Column('institucion_asupiciante', sa.String(length=130), nullable=False),
    sa.Column('funcion', sa.String(length=80), nullable=False),
    sa.Column('fecha_inicio', sa.Date(), nullable=False),
    sa.Column('fecha_fin', sa.Date(), nullable=True),
    sa.ForeignKeyConstraint(['id_persona'], ['datos_personales.identificacion'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_meritos_distinciones_id'), 'meritos_distinciones', ['id'], unique=False)
    op.create_table('ponencias_exposiciones',
    sa.Column('id', postgresql.UUID(), server_default=sa.text('uuid_generate_v4()'), nullable=False),
    sa.Column('id_persona', sa.String(length=10), nullable=False),
    sa.Column('tema', sa.String(length=150), nullable=False),
    sa.Column('institucion_organizadora', sa.String(length=80), nullable=False),
    sa.Column('evento', sa.String(length=120), nullable=False),
    sa.Column('caracter', sa.String(length=13), nullable=False),
    sa.Column('lugar', sa.String(length=120), nullable=True),
    sa.Column('fecha', sa.Date(), nullable=False),
    sa.ForeignKeyConstraint(['id_persona'], ['datos_personales.identificacion'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_ponencias_exposiciones_id'), 'ponencias_exposiciones', ['id'], unique=False)
    op.create_table('formacion_academica_personal',
    sa.Column('id', postgresql.UUID(), server_default=sa.text('uuid_generate_v4()'), nullable=False),
    sa.Column('id_persona', sa.String(length=10), nullable=False),
    sa.Column('id_pais_estudio', sa.Integer(), nullable=False),
    sa.Column('id_ies', postgresql.UUID(), nullable=True),
    sa.Column('nombre_ies', sa.String(length=150), nullable=True),
    sa.Column('id_nivel', postgresql.UUID(), nullable=False),
    sa.Column('id_grado', postgresql.UUID(), nullable=True),
    sa.Column('nombre_titulo', sa.String(length=150), nullable=False),
    sa.Column('id_campo_detallado', postgresql.UUID(), nullable=False),
    sa.Column('estado', sa.Enum('TERMINADA', 'CURSANDO', name='estadoformacion'), nullable=False),
    sa.Column('fecha_inicio', sa.Date(), nullable=False),
    sa.Column('fecha_fin', sa.Date(), nullable=True),
    sa.Column('registro_senescyt', sa.String(length=20), nullable=True),
    sa.Column('fecha_obtencion_titulo', sa.Date(), nullable=True),
    sa.Column('lugar', sa.String(length=120), nullable=False),
    sa.Column('posse_beca', sa.String(length=2), nullable=True),
    sa.Column('id_tipo_beca', postgresql.UUID(), nullable=True),
    sa.Column('monto_beca', sa.Numeric(precision=8, scale=2), nullable=True),
    sa.Column('id_financiamiento', postgresql.UUID(), nullable=True),
    sa.Column('descripcion', sa.String(length=100), nullable=True),
    sa.ForeignKeyConstraint(['id_campo_detallado'], ['campo_educativo_detallado.id'], ),
    sa.ForeignKeyConstraint(['id_financiamiento'], ['financiamiento_beca.id'], ),
    sa.ForeignKeyConstraint(['id_grado'], ['grados.id'], ),
    sa.ForeignKeyConstraint(['id_ies'], ['ies_nacionales.id'], ),
    sa.ForeignKeyConstraint(['id_nivel'], ['nivel_educativo.id'], ),
    sa.ForeignKeyConstraint(['id_pais_estudio'], ['paises.id'], ),
    sa.ForeignKeyConstraint(['id_persona'], ['datos_personales.identificacion'], ),
    sa.ForeignKeyConstraint(['id_tipo_beca'], ['tipo_beca.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_formacion_academica_personal_id'), 'formacion_academica_personal', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_formacion_academica_personal_id'), table_name='formacion_academica_personal')
    op.drop_table('formacion_academica_personal')
    op.drop_index(op.f('ix_ponencias_exposiciones_id'), table_name='ponencias_exposiciones')
    op.drop_table('ponencias_exposiciones')
    op.drop_index(op.f('ix_meritos_distinciones_id'), table_name='meritos_distinciones')
    op.drop_table('meritos_distinciones')
    op.drop_index(op.f('ix_experiencia_laboral_personal_id'), table_name='experiencia_laboral_personal')
    op.drop_table('experiencia_laboral_personal')
    op.drop_index(op.f('ix_comprension_idiomas_id'), table_name='comprension_idiomas')
    op.drop_table('comprension_idiomas')
    op.drop_index(op.f('ix_capacitaciones_facilitadores_id'), table_name='capacitaciones_facilitadores')
    op.drop_table('capacitaciones_facilitadores')
    # ### end Alembic commands ###