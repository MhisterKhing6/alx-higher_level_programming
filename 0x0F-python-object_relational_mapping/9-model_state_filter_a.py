#!/usr/bin/python3
"""
List all states that contains an A in the database
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
    result = session.query(State).filter(State.name.like('%a%'))\
        .order_by(State.id)
    if result:
        for instance in result:
            print(f'{instance.id}: {instance.name}')
