"""ini

Revision ID: 9620d7dcc16d
Revises: 5b54301c1c0e
Create Date: 2024-08-03 01:08:27.120149

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9620d7dcc16d'
down_revision: Union[str, None] = '5b54301c1c0e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('session_requests',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('trainer_uid', sa.String(), nullable=True),
    sa.Column('member_uid', sa.String(), nullable=True),
    sa.Column('requested_sessions', sa.Integer(), nullable=True),
    sa.Column('status', sa.String(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['member_uid'], ['members.uid'], ),
    sa.ForeignKeyConstraint(['trainer_uid'], ['trainers.uid'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_session_requests_id'), 'session_requests', ['id'], unique=False)
    op.add_column('members', sa.Column('fcm_tokens', sa.ARRAY(sa.String()), nullable=True))
    op.add_column('members', sa.Column('last_active', sa.DateTime(), nullable=True))
    op.add_column('trainers', sa.Column('fcm_tokens', sa.ARRAY(sa.String()), nullable=True))
    op.add_column('trainers', sa.Column('last_active', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('trainers', 'last_active')
    op.drop_column('trainers', 'fcm_tokens')
    op.drop_column('members', 'last_active')
    op.drop_column('members', 'fcm_tokens')
    op.drop_index(op.f('ix_session_requests_id'), table_name='session_requests')
    op.drop_table('session_requests')
    # ### end Alembic commands ###