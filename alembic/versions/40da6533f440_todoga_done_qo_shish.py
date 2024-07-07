"""Todoga done qo'shish

Revision ID: 40da6533f440
Revises: 
Create Date: 2024-07-07 05:30:10.390584

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '40da6533f440'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('todo', sa.Column('done', sa.Boolean(), default=False))
    op.execute('UPDATE todo SET done = false WHERE done IS NULL')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('todo', 'done')
