"""Add one-to-one author user relationship

Revision ID: 4eb3c7ea0a33
Revises: 0fcc63379ce0
Create Date: 2023-08-10 11:44:19.128663

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4eb3c7ea0a33'
down_revision = '0fcc63379ce0'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('authors', sa.Column('user_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'authors', 'users', ['user_id'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'authors', type_='foreignkey')
    op.drop_column('authors', 'user_id')
    # ### end Alembic commands ###
