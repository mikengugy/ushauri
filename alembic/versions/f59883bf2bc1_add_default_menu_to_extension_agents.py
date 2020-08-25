"""Add default menu to extension agents

Revision ID: f59883bf2bc1
Revises: 9268c216b998
Create Date: 2018-03-16 18:32:03.909151

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "f59883bf2bc1"
down_revision = "9268c216b998"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "ivrmenu", sa.Column("menu_agentcurrent", sa.Integer(), nullable=True)
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("ivrmenu", "menu_agentcurrent")
    # ### end Alembic commands ###