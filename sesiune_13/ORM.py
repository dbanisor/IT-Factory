from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

# CONNECT TO DB

engine = create_engine("sqlite:///users.db")

# CREATE TABLES

Base.metadata.create_all(engine)

# START SESSION

Session = sessionmaker(bind=engine)
session = Session()

# ADD USER

u = User(name="Andrei", age=20)
u2 = User(name="Eva", age=27)

# session.add(u)
# session.add(u2)
#
# session.commit()

# QUERY ALL USERS

users = session.query(User).all()
for user in users:
    print(user.id, user.name, user.age)

# UPDATE USER

print("*" * 50)

user = session.query(User).filter_by(name="Eva").first()
user.age = 30
session.commit()

users = session.query(User).all()
for user in users:
    print(user.id, user.name, user.age)
