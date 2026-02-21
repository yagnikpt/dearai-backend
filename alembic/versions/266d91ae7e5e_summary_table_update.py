"""summary_table_update

Revision ID: 266d91ae7e5e
Revises: b2252b83d45e
Create Date: 2026-02-18 23:45:56.529225

"""

from typing import Sequence

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "266d91ae7e5e"
down_revision: str | None = "b2252b83d45e"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
