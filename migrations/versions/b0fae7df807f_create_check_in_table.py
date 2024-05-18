"""Create check_in table

Revision ID: b0fae7df807f
Revises: d22ebff61561
Create Date: 2024-05-18 17:45:22.188313

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b0fae7df807f'
down_revision = 'd22ebff61561'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('check_in',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('checkin_date', sa.Date(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.user_id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('age',
               existing_type=sa.INTEGER(),
               type_=sa.String(length=120),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('age',
               existing_type=sa.String(length=120),
               type_=sa.INTEGER(),
               existing_nullable=True)

    op.drop_table('check_in')
    # ### end Alembic commands ###