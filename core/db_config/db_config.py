from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError

from core.constant import (
    BOLS_STORIS,
    FUTURE_MAN,
    GIF_FOR_BOLL,
    GIF_FOR_LOVE,
    LOVE_STORIS,
    THIS_RELATION
    )

engine = create_engine('sqlite:///db.sqlite3')
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()


class BaseTable(Base):
    __abstract__ = True

    @classmethod
    def load_data(cls, data_list):
        for name in data_list:
            instance = cls(name=name)
            try:
                session.add(instance)
                session.commit()
            except IntegrityError:
                session.rollback()
                print(f"Ошибка: данные {name} уже "
                      "существуют или нарушена уникальность значений.")


class Subscriber(Base):
    """Модель подписчиков"""
    __tablename__ = 'subscribers'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    lastname = Column(String)
    chat_id = Column(Integer, unique=True)
    user_username = Column(Integer)

    def __repr__(self):
        return f'Пользователь {self.name}, chat_id {self.chat_id}'


class YesAndNo(BaseTable):
    """Модель Да/Нет + что то для Шара"""
    __tablename__ = 'YesAndNo'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)

    def __repr__(self):
        return f'{self.name}'


class Stikers_for_ball(BaseTable):
    """Модель для стикеров шара"""
    __tablename__ = 'Ball_Stiker'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)

    def __repr__(self):
        return f'{self.name}'


class LoveYesAndNo(BaseTable):
    """Модель ответов любит не любит"""
    __tablename__ = 'LoveYesAndNo'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True,)

    def __repr__(self):
        return f'{self.name}'


class Stikers_for_love(BaseTable):
    """Модель стикеров для любви"""
    __tablename__ = 'Love_Stiker'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)

    def __repr__(self):
        return f'{self.name}'


class This_Relation(BaseTable):
    """Модель ответов любит есть ли будущее у этих отношений"""
    __tablename__ = 'Relation'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True,)

    def __repr__(self):
        return f'{self.name}'


class Future_Man(BaseTable):
    """Модель ответов Чего ждать в любви с этим человеком?"""
    __tablename__ = 'Future_Man'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True,)

    def __repr__(self):
        return f'{self.name}'


Base.metadata.create_all(engine)

Stikers_for_love.load_data(GIF_FOR_LOVE)
Stikers_for_ball.load_data(GIF_FOR_BOLL)
YesAndNo.load_data(BOLS_STORIS)
LoveYesAndNo.load_data(LOVE_STORIS)
This_Relation.load_data(THIS_RELATION)
Future_Man.load_data(FUTURE_MAN)
