from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import create_session
# from sqlalchemy.orm import contains_eager, joinedload
from sqlalchemy.orm import relationship
from datetime import datetime


#Create the engine and get the metadata
Base = declarative_base()

engine = create_engine(
    'mysql+pymysql://pythontest:123@localhost/SimpleCompanyDB?charset=utf8',
    connect_args = {
        # 'port': 3306
    },
    # echo='debug',
    echo_pool=True
)
metadata = MetaData(bind=engine)


# print table names:
print( engine.table_names() )

#Reflect each database table we need to use, using metadata
# class Company(Base):
#     __table__ = Table('Company', metadata, autoload=True)
#     orders = relationship("Order", backref="customer")

company = Table('company', meta, autoload=True, autoload_with=engine)
print( dir(company) )
