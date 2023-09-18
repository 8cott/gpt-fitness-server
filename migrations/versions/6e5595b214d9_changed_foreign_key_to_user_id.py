"""changed foreign key to user_id

Revision ID: 6e5595b214d9
Revises: ad7a62367341
Create Date: 2023-09-15 13:55:38.180866

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6e5595b214d9'
down_revision = 'ad7a62367341'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('saved_plans', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user_id', sa.Integer(), nullable=True))
        batch_op.drop_constraint('saved_plans_username_fkey', type_='foreignkey')
        batch_op.create_foreign_key(None, 'users', ['user_id'], ['id'])
        batch_op.drop_column('username')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('saved_plans', schema=None) as batch_op:
        batch_op.add_column(sa.Column('username', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key('saved_plans_username_fkey', 'users', ['username'], ['username'])
        batch_op.drop_column('user_id')

    # ### end Alembic commands ###