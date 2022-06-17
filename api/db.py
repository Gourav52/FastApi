from databases import Database
from sqlalchemy import (
    Column,
    Integer,
    String,
    create_engine,
    MetaData,
    Table
)


DATABASE_URL = "mysql://root:@localhost/articledb"

engine = create_engine(DATABASE_URL)

metadata = MetaData()

User = Table(
    "user",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("username", String(100)),
    Column("password", String(200)),
)

Article = Table(
    "article",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("title", String(100)),
    Column("description", String(500)),
)

# querybuilder

database = Database(DATABASE_URL)
