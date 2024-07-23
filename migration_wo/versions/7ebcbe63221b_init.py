"""init

Revision ID: 7ebcbe63221b
Revises: 
Create Date: 2024-07-22 14:10:20.946377

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7ebcbe63221b'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('quests',
    sa.Column('quest_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('trainer_id', sa.String(), nullable=False),
    sa.Column('member_id', sa.String(), nullable=False),
    sa.Column('status', sa.Enum('NOT_STARTED', 'COMPLETED', 'DEADLINE_PASSED', name='queststatus'), nullable=True),
    sa.Column('workout_date', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.PrimaryKeyConstraint('quest_id')
    )
    op.create_table('session_type_map',
    sa.Column('session_type_id', sa.Integer(), nullable=False),
    sa.Column('session_type', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('session_type_id')
    )
    op.create_index(op.f('ix_session_type_map_session_type_id'), 'session_type_map', ['session_type_id'], unique=False)
    op.create_table('workout_parts',
    sa.Column('workout_part_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('workout_part_name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('workout_part_id'),
    sa.UniqueConstraint('workout_part_name')
    )
    op.create_table('workouts',
    sa.Column('workout_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('workout_name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('workout_id'),
    sa.UniqueConstraint('workout_name')
    )
    op.create_table('session_id_mapping',
    sa.Column('session_id', sa.Integer(), nullable=False),
    sa.Column('session_type_id', sa.Integer(), nullable=True),
    sa.Column('workout_date', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.Column('member_id', sa.String(), nullable=False),
    sa.Column('trainer_id', sa.String(), nullable=True),
    sa.Column('is_pt', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['session_type_id'], ['session_type_map.session_type_id'], ),
    sa.PrimaryKeyConstraint('session_id')
    )
    op.create_index(op.f('ix_session_id_mapping_session_id'), 'session_id_mapping', ['session_id'], unique=False)
    op.create_table('workout_key_name_map',
    sa.Column('workout_key_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('workout_id', sa.Integer(), nullable=False),
    sa.Column('workout_part_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['workout_id'], ['workouts.workout_id'], ),
    sa.ForeignKeyConstraint(['workout_part_id'], ['workout_parts.workout_part_id'], ),
    sa.PrimaryKeyConstraint('workout_key_id')
    )
    op.create_table('quest_workouts',
    sa.Column('quest_id', sa.Integer(), nullable=False),
    sa.Column('workout_key', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['quest_id'], ['quests.quest_id'], ),
    sa.ForeignKeyConstraint(['workout_key'], ['workout_key_name_map.workout_key_id'], ),
    sa.PrimaryKeyConstraint('quest_id', 'workout_key'),
    sa.UniqueConstraint('quest_id', 'workout_key', name='uq_quest_workout')
    )
    op.create_table('session',
    sa.Column('session_id', sa.Integer(), nullable=False),
    sa.Column('workout_key', sa.Integer(), nullable=False),
    sa.Column('set_num', sa.Integer(), nullable=False),
    sa.Column('weight', sa.Float(), nullable=False),
    sa.Column('reps', sa.Integer(), nullable=False),
    sa.Column('rest_time', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['session_id'], ['session_id_mapping.session_id'], ),
    sa.ForeignKeyConstraint(['workout_key'], ['workout_key_name_map.workout_key_id'], ),
    sa.PrimaryKeyConstraint('session_id', 'workout_key', 'set_num')
    )
    op.create_table('quest_workout_sets',
    sa.Column('quest_id', sa.Integer(), nullable=False),
    sa.Column('workout_key', sa.Integer(), nullable=False),
    sa.Column('set_number', sa.Integer(), nullable=False),
    sa.Column('weight', sa.Float(), nullable=False),
    sa.Column('reps', sa.Integer(), nullable=False),
    sa.Column('rest_time', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['quest_id', 'workout_key'], ['quest_workouts.quest_id', 'quest_workouts.workout_key'], name='fk_quest_workout_set_workout'),
    sa.PrimaryKeyConstraint('quest_id', 'workout_key', 'set_number')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('quest_workout_sets')
    op.drop_table('session')
    op.drop_table('quest_workouts')
    op.drop_table('workout_key_name_map')
    op.drop_index(op.f('ix_session_id_mapping_session_id'), table_name='session_id_mapping')
    op.drop_table('session_id_mapping')
    op.drop_table('workouts')
    op.drop_table('workout_parts')
    op.drop_index(op.f('ix_session_type_map_session_type_id'), table_name='session_type_map')
    op.drop_table('session_type_map')
    op.drop_table('quests')
    # ### end Alembic commands ###