from database import Base, Column, VARCHAR, LargeBinary, Integer


class UserDataAccessObject(Base):
    __tablename__ = "users_tbl"
    id = Column(Integer, primary_key=True, autoincrement=True, unique=True, nullable=False)
    user = Column(VARCHAR(512), unique=True, nullable=False)
    token = Column(LargeBinary, nullable=False)

    def __init__(self, user=None, token=None):
        self.user = user
        self.token = token

    def __repr__(self): return "<User %r>" % self.__dict__
