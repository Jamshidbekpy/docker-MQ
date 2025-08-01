"""update models

Revision ID: 28445bc88559
Revises: 3911ea6076a4
Create Date: 2025-07-29 13:39:50.878713

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '28445bc88559'
down_revision: Union[str, Sequence[str], None] = '3911ea6076a4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tasks', sa.Column('created_at', sa.Date(), nullable=False))
    op.add_column('tasks', sa.Column('updated_at', sa.Date(), nullable=False))
    op.add_column('users', sa.Column('created_at', sa.Date(), nullable=False))
    op.add_column('users', sa.Column('updated_at', sa.Date(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'updated_at')
    op.drop_column('users', 'created_at')
    op.drop_column('tasks', 'updated_at')
    op.drop_column('tasks', 'created_at')
    # ### end Alembic commands ###
