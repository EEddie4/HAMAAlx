#!/usr/bin/python3
"""
python script that ---
"""

import re
import sys
from model_state import Base, State

from sqlalchemy import (create_engine)
from sqlalchemy import select
from sqlalchemy.orm import Session

if __name__ == "__main__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], str(sys.argv[2]), sys.argv[3]), pool_pre_ping=True)

    session = Session(engine)
    req = select(State).where(State.id == 1)
    result = session.execute(req)
    i = 1
    tab = result.scalars().all()
    print(tab)
    """if len(tab) == 0:
        print("Nothing")
    else:
        print("1: ", tab[0].name)"""
