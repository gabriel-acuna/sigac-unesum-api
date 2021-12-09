"""3 modelos nuevos en dath

Revision ID: 6f4de2320d9d
Revises: f1b81398bf83
Create Date: 2021-12-09 12:53:30.325279

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '6f4de2320d9d'
down_revision = 'f1b81398bf83'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('evaluaciones_personal',
    sa.Column('id', postgresql.UUID(), server_default=sa.text('uuid_generate_v4()'), nullable=False),
    sa.Column('id_persona', sa.String(length=10), nullable=True),
    sa.Column('desde', sa.Date(), nullable=False),
    sa.Column('hasta', sa.Date(), nullable=False),
    sa.Column('puntaje', sa.Numeric(precision=4, scale=2), nullable=False),
    sa.Column('calificacion', sa.String(length=60), nullable=False),
    sa.ForeignKeyConstraint(['id_persona'], ['datos_personales.identificacion'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_evaluaciones_personal_id'), 'evaluaciones_personal', ['id'], unique=False)
    op.create_table('informacion_reproductiva_personal',
    sa.Column('id', postgresql.UUID(), server_default=sa.text('uuid_generate_v4()'), nullable=False),
    sa.Column('id_persona', sa.String(length=10), nullable=True),
    sa.Column('estado', sa.String(length=30), nullable=False),
    sa.Column('inicio', sa.Date(), nullable=False),
    sa.Column('fin', sa.Date(), nullable=False),
    sa.ForeignKeyConstraint(['id_persona'], ['datos_personales.identificacion'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_informacion_reproductiva_personal_id'), 'informacion_reproductiva_personal', ['id'], unique=False)
    op.create_table('servidores_desvinculados',
    sa.Column('id', postgresql.UUID(), server_default=sa.text('uuid_generate_v4()'), nullable=False),
    sa.Column('institucion', sa.String(length=120), nullable=True),
    sa.Column('ruc', sa.String(length=13), nullable=True),
    sa.Column('id_persona', sa.String(length=10), nullable=True),
    sa.Column('fecha_ingreso', sa.Date(), nullable=False),
    sa.Column('fecha_salida', sa.Date(), nullable=False),
    sa.Column('nombre_planta', sa.String(length=120), nullable=True),
    sa.Column('id_regimen', postgresql.UUID(), nullable=False),
    sa.Column('id_modalidad', postgresql.UUID(), nullable=False),
    sa.Column('grupo_ocupacional', sa.String(length=120), nullable=True),
    sa.Column('id_motivo_desvinculacion', postgresql.UUID(), nullable=True),
    sa.Column('pago_liquidacion', sa.String(length=2), nullable=False),
    sa.Column('fecha_pago', sa.Date(), nullable=True),
    sa.Column('valor_cancelado', sa.Numeric(precision=9, scale=2), nullable=False),
    sa.Column('motivo_incumplimiento', sa.String(length=120), nullable=True),
    sa.ForeignKeyConstraint(['id_modalidad'], ['modalidades_contractuales.id'], ),
    sa.ForeignKeyConstraint(['id_motivo_desvinculacion'], ['motivos_desvinculacion.id'], ),
    sa.ForeignKeyConstraint(['id_persona'], ['datos_personales.identificacion'], ),
    sa.ForeignKeyConstraint(['id_regimen'], ['regimen_disciplinario.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_servidores_desvinculados_id'), 'servidores_desvinculados', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_servidores_desvinculados_id'), table_name='servidores_desvinculados')
    op.drop_table('servidores_desvinculados')
    op.drop_index(op.f('ix_informacion_reproductiva_personal_id'), table_name='informacion_reproductiva_personal')
    op.drop_table('informacion_reproductiva_personal')
    op.drop_index(op.f('ix_evaluaciones_personal_id'), table_name='evaluaciones_personal')
    op.drop_table('evaluaciones_personal')
    # ### end Alembic commands ###