"""empty message

Revision ID: b5a6cf2c6687
Revises: 0bf7832d16d0
Create Date: 2023-05-20 12:09:25.381964

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b5a6cf2c6687'
down_revision = '0bf7832d16d0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('Cliente', schema=None) as batch_op:
        batch_op.alter_column('rut',
               existing_type=sa.INTEGER(),
               type_=sa.String(length=10),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('Cliente', schema=None) as batch_op:
        batch_op.alter_column('rut',
               existing_type=sa.String(length=10),
               type_=sa.INTEGER(),
               existing_nullable=False)

    # ### end Alembic commands ###
