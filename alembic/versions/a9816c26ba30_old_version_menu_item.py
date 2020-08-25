"""Old version Menu item

Revision ID: a9816c26ba30
Revises: b8c6b83d1377
Create Date: 2018-03-17 06:39:08.237331

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = "a9816c26ba30"
down_revision = "b8c6b83d1377"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("menuitem")
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "menuitem",
        sa.Column("item_id", mysql.VARCHAR(length=12), nullable=False),
        sa.Column(
            "item_type",
            mysql.INTEGER(display_width=11),
            autoincrement=False,
            nullable=True,
        ),
        sa.Column("item_desc", mysql.TEXT(), nullable=True),
        sa.Column(
            "item_pos",
            mysql.INTEGER(display_width=11),
            autoincrement=False,
            nullable=True,
        ),
        sa.Column("group_id", mysql.VARCHAR(length=12), nullable=False),
        sa.Column("menu_id", mysql.VARCHAR(length=12), nullable=False),
        sa.Column("next_item", mysql.VARCHAR(length=12), nullable=True),
        sa.ForeignKeyConstraint(
            ["group_id", "menu_id"],
            ["ivrmenu.group_id", "ivrmenu.menu_id"],
            name="fk_menuitem_group_id_ivrmenu",
            ondelete="CASCADE",
        ),
        sa.ForeignKeyConstraint(
            ["next_item"], ["menuitem.item_id"], name="fk_menuitem_next_item_menuitem"
        ),
        sa.PrimaryKeyConstraint("item_id"),
        mysql_default_charset="latin1",
        mysql_engine="InnoDB",
    )
    # ### end Alembic commands ###