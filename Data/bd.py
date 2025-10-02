from pony.orm import *
from menu import menu
from classes import *
db.bind(provider='sqlite', filename='data.db', create_db=True)
db.generate_mapping(create_tables=True)

with db_session:

    while 1:
        obj=menu()
        commit()