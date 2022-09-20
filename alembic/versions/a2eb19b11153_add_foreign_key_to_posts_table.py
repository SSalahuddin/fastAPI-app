"""add foreign key to posts table

Revision ID: a2eb19b11153
Revises: dccee016694b
Create Date: 2022-09-18 14:45:06.381830

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a2eb19b11153'
down_revision = 'dccee016694b'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('postsORM', sa.Column('user_id', sa.Integer(), nullable=False)),
    op.create_foreign_key('posts_users_fk', source_table="postsORM", referent_table="usersORM", local_cols=['user_id'], remote_cols=['id'], ondelete="CASCADE")
    pass


def downgrade():
    op.drop_constraint('posts_users_fk', table_name="postsORM")
    op.drop_column('postsORM', 'user_id')
    pass