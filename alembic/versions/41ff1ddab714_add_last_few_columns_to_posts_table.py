"""add last few columns to posts table

Revision ID: 41ff1ddab714
Revises: a2eb19b11153
Create Date: 2022-09-18 16:18:32.595784

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '41ff1ddab714'
down_revision = 'a2eb19b11153'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('postsORM', sa.Column('published', sa.Boolean(), nullable=False, server_default='TRUE'))
    op.add_column('postsORM', sa.Column('created_At', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()')))
    pass


def downgrade():
    op.drop_column('postsORM', 'published')
    op.drop_column('postsORM', 'created_At')
    pass
