"""modifying user_trainer map database

Revision ID: dc55ed0449b1
Revises: 529a0ea627ee
Create Date: 2024-07-09 11:23:13.022032

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'dc55ed0449b1'
down_revision: Union[str, None] = '529a0ea627ee'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('trainer_user_mapping')
    op.create_table('trainer_user_mapping',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('trainer_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['trainer_id'], ['trainers.trainer_id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.user_id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_trainer_user_mapping_id'), 'trainer_user_mapping', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_trainer_user_mapping_id'), table_name='trainer_user_mapping')
    op.drop_table('trainer_user_mapping')
    # ### end Alembic commands ###