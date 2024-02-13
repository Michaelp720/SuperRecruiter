"""empty message

Revision ID: 65dd81fc61d8
Revises: c78a76335310
Create Date: 2024-02-13 08:30:45.975436

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '65dd81fc61d8'
down_revision = 'c78a76335310'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('teams',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('team_name', sa.String(), nullable=True),
    sa.Column('allignment', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_teams'))
    )
    op.create_table('capes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('cape_name', sa.String(), nullable=True),
    sa.Column('classification', sa.String(), nullable=True),
    sa.Column('powers', sa.String(), nullable=True),
    sa.Column('allignment', sa.String(), nullable=True),
    sa.Column('team_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['team_id'], ['teams.id'], name=op.f('fk_capes_team_id_teams')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_capes')),
    sa.UniqueConstraint('cape_name', name=op.f('uq_capes_cape_name'))
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('capes')
    op.drop_table('teams')
    # ### end Alembic commands ###
