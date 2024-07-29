"""creatiing new database

Revision ID: 0ff236b1bdf8
Revises: 
Create Date: 2024-07-08 17:50:13.440826

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0ff236b1bdf8'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('session_id_mapping',
    sa.Column('session_id', sa.Integer(), nullable=False),
    sa.Column('workout_date', sa.String(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('trainer_uid', sa.Integer(), nullable=False),
    sa.Column('is_pt', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('session_id')
    )
    op.create_index(op.f('ix_session_id_mapping_session_id'), 'session_id_mapping', ['session_id'], unique=False)
    op.create_table('trainers',
    sa.Column('trainer_uid', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('trainer_uid')
    )
    op.create_index(op.f('ix_trainers_email'), 'trainers', ['email'], unique=True)
    op.create_index(op.f('ix_trainers_trainer_id'), 'trainers', ['trainer_uid'], unique=True)
    op.create_table('users',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('user_id')
    )
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    op.create_index(op.f('ix_users_user_id'), 'users', ['user_id'], unique=True)
    op.create_table('workout_key_name_mapping',
    sa.Column('workout_key', sa.Integer(), nullable=False),
    sa.Column('workout_name', sa.String(), nullable=False),
    sa.Column('workout_part', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('workout_key')
    )
    op.create_table('session',
    sa.Column('session_id', sa.Integer(), nullable=False),
    sa.Column('workout_key', sa.Integer(), nullable=False),
    sa.Column('set_num', sa.Integer(), nullable=False),
    sa.Column('weight', sa.Float(), nullable=False),
    sa.ForeignKeyConstraint(['session_id'], ['session_id_mapping.session_id'], ),
    sa.ForeignKeyConstraint(['workout_key'], ['workout_key_name_mapping.workout_key'], ),
    sa.PrimaryKeyConstraint('session_id', 'workout_key', 'set_num')
    )
    op.create_table('trainer_user_mapping',
    sa.Column('trainer_uid', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['trainer_uid'], ['trainers.trainer_uid'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_id'], ['users.user_id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('trainer_uid', 'user_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('trainer_user_mapping')
    op.drop_table('session')
    op.drop_table('workout_key_name_mapping')
    op.drop_index(op.f('ix_users_user_id'), table_name='users')
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_table('users')
    op.drop_index(op.f('ix_trainers_trainer_id'), table_name='trainers')
    op.drop_index(op.f('ix_trainers_email'), table_name='trainers')
    op.drop_table('trainers')
    op.drop_index(op.f('ix_session_id_mapping_session_id'), table_name='session_id_mapping')
    op.drop_table('session_id_mapping')
    # ### end Alembic commands ###
