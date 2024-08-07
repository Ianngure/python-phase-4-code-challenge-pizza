"""Updated models

Revision ID: d88d741937ad
Revises: 0421b3616322
Create Date: 2024-07-08 00:20:54.800443

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd88d741937ad'
down_revision = '0421b3616322'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('pizzas', 'name',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('pizzas', 'ingredients',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('restaurant_pizzas', 'pizza_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('restaurant_pizzas', 'restaurant_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('restaurants', 'name',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('restaurants', 'address',
               existing_type=sa.VARCHAR(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('restaurants', 'address',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('restaurants', 'name',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('restaurant_pizzas', 'restaurant_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('restaurant_pizzas', 'pizza_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('pizzas', 'ingredients',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('pizzas', 'name',
               existing_type=sa.VARCHAR(),
               nullable=True)
    # ### end Alembic commands ###
