#!/usr/bin/python3
"""
List the first states from the database
"""
import sys
from sqlalchemy.orm import sessionmaker

from model_state import State

from sqlalchemy import (create_engine)

if __name__ == "__main__":
    # get a session
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.
        format(sys.argv[1], sys.argv[2], sys.argv[3]),
        pool_pre_ping=True
    )
    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.query(State).order_by(State.id).first()
    if result:
        print('{}: {}'.format(result.id, result.name))
    else:
        print("Nothing")
