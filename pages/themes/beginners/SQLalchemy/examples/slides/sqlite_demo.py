from sqlalchemy import create_engine

engine = create_engine('sqlite:///:memory:')
engine.execute("select 'Hello, World!'").scalar()
