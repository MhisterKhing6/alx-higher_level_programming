#!/usr/bin/python3

"""List all cites related to states"""

from model_city import City, Base
from model_state import State
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    # create engine
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'
        .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    # create table
    Base.metadata.create_all(bind=engine)
    # create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Perform query
    for state, city in session.query(State, City)\
            .filter(State.id == City.state_id).order_by(City.id):
        print('{}: ({}) {}'.format(state.name, city.id, city.name))
