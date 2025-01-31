"""empty message

Revision ID: fb89aa90c882
Revises: 43e394aaee62
Create Date: 2025-01-31 14:37:06.042654

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fb89aa90c882'
down_revision = '43e394aaee62'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user', 'is_admin',
               existing_type=sa.BOOLEAN(),
               type_=sa.Text(),
               existing_nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user', 'is_admin',
               existing_type=sa.Text(),
               type_=sa.BOOLEAN(),
               existing_nullable=True)
    # ### end Alembic commands ###
