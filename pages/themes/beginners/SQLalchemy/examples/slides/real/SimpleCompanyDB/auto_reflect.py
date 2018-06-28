# from sqlalchemy import *
# for reflection:
from sqlalchemy import  MetaData, Table
from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine import reflection
# from sqlalchemy.orm import create_session
# from sqlalchemy.orm import contains_eager, joinedload
# from sqlalchemy.orm import relationship
# from datetime import datetime


#Create the engine
# Base = declarative_base()
engine = create_engine(
    'mysql+pymysql://demo:123@localhost/SimpleCompanyDB?charset=utf8',
    connect_args = {
        # 'port': 3306
    },
    # echo='debug',
    echo_pool=True
)


insp = reflection.Inspector.from_engine(engine)
print(insp.get_table_names())

# print( insp.get_columns("employee"))


# # get the metadata
# metadata = MetaData(bind=engine)

# # print table names:
# print(f'tables: {engine.table_names()}')

# #Reflect each database table we need to use, using metadata
# company = Table('company', metadata, autoload=True, autoload_with=engine)
# employee = Table('employee', metadata, autoload=True, autoload_with=engine)
# print("Company table columns:")
# for c in company.columns:
#   print(c)

# # print content of employees
# print(repr(employee))
# # insert a record:
# ins = employee.insert().values(employee_name='Pesho')
# print(ins)

# Session = sessionmaker(bind=engine)
