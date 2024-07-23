"""workout table modified
Revision ID: 434a972515a6
Revises: 7da87fa49dd1
Create Date: 2024-07-15 18:11:24.077567
"""
from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = '434a972515a6'
down_revision: Union[str, None] = '7da87fa49dd1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    
    # First, drop the foreign key constraint in the session table
    op.drop_constraint('session_workout_key_fkey', 'session', type_='foreignkey')
    
    # Now we can safely drop the tables
    op.drop_table('workout_key_name_mapping')
    op.drop_table('workout_part_id_name_map')
    
    # Create new tables
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
    op.create_table('workout_key_name_map',
        sa.Column('workout_key_id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('workout_id', sa.Integer(), nullable=False),
        sa.Column('workout_part_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['workout_id'], ['workouts.workout_id'], ),
        sa.ForeignKeyConstraint(['workout_part_id'], ['workout_parts.workout_part_id'], ),
        sa.PrimaryKeyConstraint('workout_key_id')
    )
    
    # Finally, add the new foreign key constraint to the session table
    op.create_foreign_key(None, 'session', 'workout_key_name_map', ['workout_key'], ['workout_key_id'])
    
    # ### end Alembic commands ###

def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'session', type_='foreignkey')
    op.create_table('workout_part_id_name_map',
        sa.Column('workout_part_id', sa.INTEGER(), server_default=sa.text("nextval('workout_part_id_name_map_workout_part_id_seq'::regclass)"), autoincrement=True, nullable=False),
        sa.Column('workout_part_name', sa.VARCHAR(), autoincrement=False, nullable=False),
        sa.PrimaryKeyConstraint('workout_part_id', name='workout_part_id_name_map_pkey'),
        postgresql_ignore_search_path=False
    )
    op.create_table('workout_key_name_mapping',
        sa.Column('workout_key', sa.INTEGER(), autoincrement=True, nullable=False),
        sa.Column('workout_name', sa.VARCHAR(), autoincrement=False, nullable=False),
        sa.Column('workout_part_id', sa.INTEGER(), autoincrement=False, nullable=False),
        sa.ForeignKeyConstraint(['workout_part_id'], ['workout_part_id_name_map.workout_part_id'], name='workout_key_name_mapping_workout_part_id_fkey'),
        sa.PrimaryKeyConstraint('workout_key', name='workout_key_name_mapping_pkey')
    )
    op.drop_table('workout_key_name_map')
    op.drop_table('workouts')
    op.drop_table('workout_parts')
    op.create_foreign_key('session_workout_key_fkey', 'session', 'workout_key_name_mapping', ['workout_key'], ['workout_key'])
    # ### end Alembic commands ###