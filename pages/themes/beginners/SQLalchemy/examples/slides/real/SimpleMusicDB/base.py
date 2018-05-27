from sqlalchemy import create_engine

mysql_engine = create_engine(
  "mysql+pymysql://user:pass@localhost/test")

pg_engine = create_engine('postgresql://usr:pass@localhost/sqlalchemy')