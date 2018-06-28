from base import Session, engine, Base
from reflected_model import Company,Employee

# generate database schema
Base.metadata.create_all(engine)

# create a new session
session = Session()

# insert data
microsoft = Company("Microsoft")
stoyan = Employee("Stoyan Vasilev")
 # add actors to movies
microsoft.actors = [matt_damon]


# persists data
session.add(microsoft)
session.add(stoyan)

# commit and close session
session.commit()
session.close()