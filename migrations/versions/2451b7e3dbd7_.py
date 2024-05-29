"""empty message

<<<<<<<< HEAD:migrations/versions/2451b7e3dbd7_.py
Revision ID: 2451b7e3dbd7
Revises: 
Create Date: 2024-05-28 17:00:46.611094
========
Revision ID: eda56976ae10
Revises: 
Create Date: 2024-05-27 22:33:17.291153
>>>>>>>> develop:migrations/versions/eda56976ae10_.py

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
<<<<<<<< HEAD:migrations/versions/2451b7e3dbd7_.py
revision = '2451b7e3dbd7'
========
revision = 'eda56976ae10'
>>>>>>>> develop:migrations/versions/eda56976ae10_.py
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('breed',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=250), nullable=False),
    sa.Column('type', sa.String(length=250), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('city',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=250), nullable=False),
    sa.Column('pet_friendly', sa.String(length=80), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('owner',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password', sa.String(length=80), nullable=False),
<<<<<<<< HEAD:migrations/versions/2451b7e3dbd7_.py
    sa.Column('address', sa.String(length=250), nullable=True),
    sa.Column('latitude', sa.Float(), nullable=True),
    sa.Column('longitude', sa.Float(), nullable=True),
========
    sa.Column('profile_picture_url', sa.String(length=200), nullable=True),
>>>>>>>> develop:migrations/versions/eda56976ae10_.py
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('name')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password', sa.String(length=80), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('pet',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('breed_id', sa.Integer(), nullable=True),
    sa.Column('sex', sa.String(length=10), nullable=False),
    sa.Column('age', sa.Integer(), nullable=False),
    sa.Column('pedigree', sa.Boolean(), nullable=False),
    sa.Column('photo', sa.String(length=100), nullable=True),
    sa.Column('owner_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['breed_id'], ['breed.id'], ),
    sa.ForeignKeyConstraint(['owner_id'], ['owner.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('pet')
    op.drop_table('user')
    op.drop_table('owner')
    op.drop_table('city')
    op.drop_table('breed')
    # ### end Alembic commands ###
