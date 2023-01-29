from sqlModels import select_engine
from sqlalchemy.orm import Session
from sqlModels.models import Number
from sqlalchemy.sql import func
import time
import datetime
from threading import Thread


def need_for_speed():
    # Get user just to see if reouting is working well
    for i in range(600):
        user_id = i
        engine = select_engine(user_id)
        session = Session(engine)
        # result = session.execute('select firstname from users where user_id=2')
        total = session.query(func.sum(Number.num).label("total")).first()
        session.close()
        if i % 100 == 0:
            print(i)
    print("finished queries")

before = datetime.datetime.now()
need_for_speed()

after = datetime.datetime.now()

print(after-before)


# print("@------@")
# with Session(select_engine(2, write=True)) as session:
#     result = session.execute('insert into followers(user_main, user_follower) values(1002, 1012)')
#     session.commit()

# # Get follower, cos I'm using this to test writing
# for i in range(10):
#     user_id = i
#     engine = select_engine(user_id)
#     session = Session(engine)
#     # result = session.execute('select * from followers where user_main=2 and user_follower=32')
#     follow = session.query(Follow).filter(Follow.user_main==2, Follow.user_follower==32).first()
#     print(user_id, session.get_bind(), [follow.user_main, follow.user_follower])
#     session.close()

# with Session(select_engine(2, write=True)) as session:
#     result = session.execute('delete from followers where user_main=2 and user_follower=32;')
#     session.commit()

# # Get follower, cos I'm using this to test writing
# for i in range(10):
#     user_id = i
#     engine = select_engine(user_id)
#     session = Session(engine)
#     # result = session.execute('select * from followers where user_main=2 and user_follower=32')
#     follow = session.query(Follow).filter(Follow.user_main==2, Follow.user_follower==32).first()
#     print(user_id, session.get_bind(), [follow.user_main, follow.user_follower] if follow else None)
#     session.close()