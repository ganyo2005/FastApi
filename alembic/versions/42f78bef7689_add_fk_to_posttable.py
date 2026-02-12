"""add fk to postTable

Revision ID: 42f78bef7689
Revises: 513b3026cf47
Create Date: 2026-02-08 12:03:49.406143

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '42f78bef7689'
down_revision: Union[str, Sequence[str], None] = '513b3026cf47'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('post',sa.Column('user_id',sa.Integer(),nullable=False))
    op.create_foreign_key('post_users_fk',source_table='post',referent_table='users',local_cols=['user_id'],remote_cols=['id'],ondelete='CASCADE')
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_constraint('post_users_fk',table_name='post')
    op.drop_column('post','user_id')

    pass

