"""initial add indexes in films

Revision ID: 07e7d6b2c9dd
Revises: 8511c68f0e8d
Create Date: 2025-01-11 15:04:36.251343

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '07e7d6b2c9dd'
down_revision: Union[str, None] = '8511c68f0e8d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index(op.f('ix_films_country'), 'films', ['country'], unique=False)
    op.create_index(op.f('ix_films_genre'), 'films', ['genre'], unique=False)
    op.create_index(op.f('ix_films_title'), 'films', ['title'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_films_title'), table_name='films')
    op.drop_index(op.f('ix_films_genre'), table_name='films')
    op.drop_index(op.f('ix_films_country'), table_name='films')
    # ### end Alembic commands ###
