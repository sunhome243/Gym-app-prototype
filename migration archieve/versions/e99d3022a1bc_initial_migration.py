"""Initial migration

Revision ID: e99d3022a1bc
Revises: 
Create Date: 2024-07-01 16:35:29.591885

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e99d3022a1bc'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('trainers',
    sa.Column('trainer_id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('hashed_password', sa.String(), nullable=False),
    sa.Column('first_name', sa.String(), nullable=True),
    sa.Column('last_name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('trainer_id')
    )
    op.create_index(op.f('ix_trainers_email'), 'trainers', ['email'], unique=True)
    op.create_index(op.f('ix_trainers_trainer_id'), 'trainers', ['trainer_id'], unique=True)
    op.create_table('users',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('hashed_password', sa.String(), nullable=True),
    sa.Column('age', sa.Integer(), nullable=True),
    sa.Column('height', sa.Double(), nullable=True),
    sa.Column('weight', sa.Double(), nullable=True),
    sa.Column('workout_level', sa.Integer(), nullable=True),
    sa.Column('workout_frequency', sa.Integer(), nullable=True),
    sa.Column('workout_goal', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('user_id')
    )
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    op.create_index(op.f('ix_users_user_id'), 'users', ['user_id'], unique=True)
    op.create_table('workout_level_mapping',
    sa.Column('workout_level', sa.Integer(), nullable=False),
    sa.Column('workout_level_name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('workout_level')
    )
    op.create_index(op.f('ix_workout_level_mapping_workout_level'), 'workout_level_mapping', ['workout_level'], unique=False)
    op.create_index(op.f('ix_workout_level_mapping_workout_level_name'), 'workout_level_mapping', ['workout_level_name'], unique=False)
    op.create_table('workout_frequency_mapping',
    sa.Column('workout_frequency', sa.Integer(), nullable=False),
    sa.Column('workout_frequency_name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('workout_frequency')
    )
    op.create_index(op.f('ix_workout_frequency_mapping_workout_frequency'), 'workout_frequency_mapping', ['workout_frequency'], unique=False)
    op.create_index(op.f('ix_workout_frequency_mapping_workout_frequency_name'), 'workout_frequency_mapping', ['workout_frequency_name'], unique=False)
    op.create_table('workout_goal_mapping',
    sa.Column('workout_goal', sa.Integer(), nullable=False),
    sa.Column('workout_goal_name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('workout_goal')
    )
    op.create_index(op.f('ix_workout_goal_mapping_workout_goal'), 'workout_goal_mapping', ['workout_goal'], unique=False)
    op.create_index(op.f('ix_workout_goal_mapping_workout_goal_name'), 'workout_goal_mapping', ['workout_goal_name'], unique=False)
    op.create_table('trainer_user_mapping',
    sa.Column('trainer_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['trainer_id'], ['trainers.trainer_id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_id'], ['users.user_id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('trainer_id', 'user_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('trainer_user_mapping')
    op.drop_index(op.f('ix_workout_goal_mapping_workout_goal_name'), table_name='workout_goal_mapping')
    op.drop_index(op.f('ix_workout_goal_mapping_workout_goal'), table_name='workout_goal_mapping')
    op.drop_table('workout_goal_mapping')
    op.drop_index(op.f('ix_workout_frequency_mapping_workout_frequency_name'), table_name='workout_frequency_mapping')
    op.drop_index(op.f('ix_workout_frequency_mapping_workout_frequency'), table_name='workout_frequency_mapping')
    op.drop_table('workout_frequency_mapping')
    op.drop_index(op.f('ix_workout_level_mapping_workout_level_name'), table_name='workout_level_mapping')
    op.drop_index(op.f('ix_workout_level_mapping_workout_level'), table_name='workout_level_mapping')
    op.drop_table('workout_level_mapping')
    op.drop_index(op.f('ix_users_user_id'), table_name='users')
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_table('users')
    op.drop_index(op.f('ix_trainers_trainer_id'), table_name='trainers')
    op.drop_index(op.f('ix_trainers_email'), table_name='trainers')
    op.drop_table('trainers')
    # ### end Alembic commands ###