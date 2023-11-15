from sqlalchemy import LargeBinary, create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
# import os
# from PIL import Image

engine = create_engine('sqlite:///subscribers.db')
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()


class Subscriber(Base):
    __tablename__ = 'subscribers'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    chat_id = Column(Integer)

    def __repr__(self):
        return f'Пользователь {self.name}, chat_id {self.chat_id}'


class YesAndNo(Base):
    __tablename__ = 'BOLS_STORIS'
    id = Column(Integer, primary_key=True)
    answer = Column(String)

    def __repr__(self):
        return f'Ответ {self.answer}'


Base.metadata.create_all(engine)

answers = ['ДА', 'НЕТ', 'МОЖЕТ БЫТЬ', 'ИДИ ВЫПЕЙ']

for answer in answers:
    new_answer = YesAndNo(answer=answer)
    session.add(new_answer)

session.commit()
