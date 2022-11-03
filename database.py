from sqlalchemy import create_engine, Column, Text, BLOB, Integer, VARCHAR, LargeBinary
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from contextlib import contextmanager
from os.path import dirname, abspath, join


debug_db_path = join(dirname(abspath(__file__)), "debug.db")
engine = create_engine(f"sqlite:///{debug_db_path}", pool_pre_ping=True)
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()


def init_debug_db():
    global Base
    Base.metadata.create_all(bind=engine)


@contextmanager
def get_session():
    global db_session
    try:
        yield db_session
    except:
        db_session.rollback()
        raise
    else:
        db_session.commit()
