from pony.orm import *
from menu import menu

db=Database()


db.generate_mapping(create_tables=True)

with db_session:

    commit()