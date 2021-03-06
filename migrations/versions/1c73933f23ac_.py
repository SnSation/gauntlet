"""empty message

Revision ID: 1c73933f23ac
Revises: 7be6e4205f71
Create Date: 2020-12-31 15:30:51.613098

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1c73933f23ac'
down_revision = '7be6e4205f71'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('trial_gauntlet', sa.Column('gauntlet_id', sa.Integer(), nullable=True))
    op.drop_constraint('trial_gauntlet_event_id_fkey', 'trial_gauntlet', type_='foreignkey')
    op.create_foreign_key(None, 'trial_gauntlet', 'gauntlet', ['gauntlet_id'], ['id'])
    op.drop_column('trial_gauntlet', 'event_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('trial_gauntlet', sa.Column('event_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'trial_gauntlet', type_='foreignkey')
    op.create_foreign_key('trial_gauntlet_event_id_fkey', 'trial_gauntlet', 'event', ['event_id'], ['id'])
    op.drop_column('trial_gauntlet', 'gauntlet_id')
    # ### end Alembic commands ###
