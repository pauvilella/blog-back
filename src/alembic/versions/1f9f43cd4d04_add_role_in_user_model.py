"""Add role in user model

Revision ID: 1f9f43cd4d04
Revises: 7c999d0c5044
Create Date: 2023-07-27 15:07:35.848192

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1f9f43cd4d04'
down_revision = '7c999d0c5044'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('role', sa.String(length=225), nullable=True))
    # ### end Alembic commands ###

    # Code typed by us (populate existing users with role='reader')
    op.execute("UPDATE users SET role='reader'")


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'role')
    # ### end Alembic commands ###
