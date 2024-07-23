"""user to member

Revision ID: 239fd439210e
Revises: 
Create Date: 2024-07-16 17:46:02.619518

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '239fd439210e'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('members',
    sa.Column('member_id', sa.String(), nullable=False),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('hashed_password', sa.String(), nullable=True),
    sa.Column('age', sa.Integer(), nullable=True),
    sa.Column('height', sa.Float(), nullable=True),
    sa.Column('weight', sa.Float(), nullable=True),
    sa.Column('workout_duration', sa.Integer(), nullable=True),
    sa.Column('workout_frequency', sa.Integer(), nullable=True),
    sa.Column('workout_goal', sa.Integer(), nullable=True),
    sa.Column('first_name', sa.String(), nullable=True),
    sa.Column('last_name', sa.String(), nullable=True),
    sa.Column('role', sa.Enum('member', 'trainer', name='userrole'), nullable=True),
    sa.PrimaryKeyConstraint('member_id')
    )
    op.create_index(op.f('ix_members_email'), 'members', ['email'], unique=True)
    op.create_index(op.f('ix_members_member_id'), 'members', ['member_id'], unique=True)
    op.create_table('trainers',
    sa.Column('trainer_id', sa.String(), nullable=False),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('hashed_password', sa.String(), nullable=False),
    sa.Column('first_name', sa.String(), nullable=True),
    sa.Column('last_name', sa.String(), nullable=True),
    sa.Column('role', sa.Enum('member', 'trainer', name='userrole'), nullable=True),
    sa.PrimaryKeyConstraint('trainer_id')
    )
    op.create_index(op.f('ix_trainers_email'), 'trainers', ['email'], unique=True)
    op.create_index(op.f('ix_trainers_trainer_id'), 'trainers', ['trainer_id'], unique=True)
    op.create_table('workout_duration_mapping',
    sa.Column('workout_duration', sa.Integer(), nullable=False),
    sa.Column('workout_duration_name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('workout_duration')
    )
    op.create_index(op.f('ix_workout_duration_mapping_workout_duration'), 'workout_duration_mapping', ['workout_duration'], unique=False)
    op.create_index(op.f('ix_workout_duration_mapping_workout_duration_name'), 'workout_duration_mapping', ['workout_duration_name'], unique=False)
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
    op.create_table('trainer_member_mapping',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('trainer_id', sa.String(), nullable=True),
    sa.Column('member_id', sa.String(), nullable=True),
    sa.Column('status', sa.Enum('pending', 'accepted', name='mappingstatus'), nullable=True),
    sa.Column('requester_id', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['member_id'], ['members.member_id'], ),
    sa.ForeignKeyConstraint(['trainer_id'], ['trainers.trainer_id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_trainer_member_mapping_id'), 'trainer_member_mapping', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_trainer_member_mapping_id'), table_name='trainer_member_mapping')
    op.drop_table('trainer_member_mapping')
    op.drop_index(op.f('ix_workout_goal_mapping_workout_goal_name'), table_name='workout_goal_mapping')
    op.drop_index(op.f('ix_workout_goal_mapping_workout_goal'), table_name='workout_goal_mapping')
    op.drop_table('workout_goal_mapping')
    op.drop_index(op.f('ix_workout_frequency_mapping_workout_frequency_name'), table_name='workout_frequency_mapping')
    op.drop_index(op.f('ix_workout_frequency_mapping_workout_frequency'), table_name='workout_frequency_mapping')
    op.drop_table('workout_frequency_mapping')
    op.drop_index(op.f('ix_workout_duration_mapping_workout_duration_name'), table_name='workout_duration_mapping')
    op.drop_index(op.f('ix_workout_duration_mapping_workout_duration'), table_name='workout_duration_mapping')
    op.drop_table('workout_duration_mapping')
    op.drop_index(op.f('ix_trainers_trainer_id'), table_name='trainers')
    op.drop_index(op.f('ix_trainers_email'), table_name='trainers')
    op.drop_table('trainers')
    op.drop_index(op.f('ix_members_member_id'), table_name='members')
    op.drop_index(op.f('ix_members_email'), table_name='members')
    op.drop_table('members')
    # ### end Alembic commands ###