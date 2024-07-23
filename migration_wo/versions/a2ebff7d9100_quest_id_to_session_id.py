"""quest id to session id

Revision ID: a2ebff7d9100
Revises: c73ae6ab574f
Create Date: 2024-07-23 14:05:29.232993

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a2ebff7d9100'
down_revision: Union[str, None] = 'c73ae6ab574f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('session_id_mapping', sa.Column('quest_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'session_id_mapping', 'quests', ['quest_id'], ['quest_id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'session_id_mapping', type_='foreignkey')
    op.drop_column('session_id_mapping', 'quest_id')
    # ### end Alembic commands ###