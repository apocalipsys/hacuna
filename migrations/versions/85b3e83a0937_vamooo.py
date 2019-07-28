"""vamooo

Revision ID: 85b3e83a0937
Revises: 
Create Date: 2019-07-28 20:15:49.906019

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '85b3e83a0937'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('admin',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=40), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.create_table('inscriptos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=20), nullable=True),
    sa.Column('apellido', sa.String(length=20), nullable=True),
    sa.Column('email', sa.String(length=40), nullable=True),
    sa.Column('telefono', sa.Integer(), nullable=True),
    sa.Column('curso_pagado', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('inscriptos')
    op.drop_table('admin')
    # ### end Alembic commands ###
