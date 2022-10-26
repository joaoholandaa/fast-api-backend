"""Nova coluna Tamanhos

Revision ID: 321c7e5b3013
Revises: 84396322ccdc
Create Date: 2022-10-26 01:07:06.365794

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '321c7e5b3013'
down_revision = '84396322ccdc'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('produto', sa.Column('tamanhos', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('produto', 'tamanhos')
    # ### end Alembic commands ###
