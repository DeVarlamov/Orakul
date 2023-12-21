import os
from sqlalchemy import DateTime, create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError
from datetime import datetime
from dotenv import load_dotenv


# from core.constant import (
#     BOLS_STORIS,
#     FUTURE_MAN,
#     GIF_FOR_BOLL,
#     GIF_FOR_LOVE,
#     LOVE_STORIS,
#     STIKERS_VORON,
#     THIS_RELATION,
#     VORON_SPECK,
#     WORK_BELT,
#     WORK_BELT_GIF
#     )

load_dotenv()

USE_SQL = bool(os.getenv('USE_SQL', False))

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
    last_prediction_time = Column(DateTime, default=datetime.utcnow)

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


class Work_Belt(BaseTable):
    """Модель ответов Чего ждать в любви с этим человеком?"""
    __tablename__ = 'Work_Belt'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True,)

    def __repr__(self):
        return f'{self.name}'


class Stikers_Work_Belt(BaseTable):
    """Модель ответов Чего ждать в любви с этим человеком?"""
    __tablename__ = 'Stikers_Work_Belt'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True,)

    def __repr__(self):
        return f'{self.name}'


class Stikers_Voron(BaseTable):
    """Модель Стикеров Ворона"""
    __tablename__ = 'Stikers_Voron'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True,)

    def __repr__(self):
        return f'{self.name}'


class Voron_Speak(BaseTable):
    """Модель ответов Ворона"""
    __tablename__ = 'Voron_Speak'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True,)

    def __repr__(self):
        return f'{self.name}'


class Texts(Base):
    """Модель Текста"""
    __tablename__ = 'text'
    id = Column(Integer, primary_key=True)
    text = Column(String)

    def __repr__(self):
        return f' {self.text}'


class Recommendations(Base):
    __tablename__ = 'Recommendations'
    id = Column(Integer, primary_key=True)
    chat_id = Column(Integer, unique=True)
    path_card = Column(String)
    pack = Column(String)
    last_prediction_time = Column(DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'{self.chat_id}'


Base.metadata.create_all(engine)

# if USE_SQL:
#     Stikers_for_love.load_data(GIF_FOR_LOVE)
#     Stikers_for_ball.load_data(GIF_FOR_BOLL)
#     YesAndNo.load_data(BOLS_STORIS)
#     LoveYesAndNo.load_data(LOVE_STORIS)
#     This_Relation.load_data(THIS_RELATION)
#     Future_Man.load_data(FUTURE_MAN)
#     Work_Belt.load_data(WORK_BELT)
#     Stikers_Work_Belt.load_data(WORK_BELT_GIF)
#     Stikers_Voron.load_data(STIKERS_VORON)
#     Voron_Speak.load_data(VORON_SPECK)
# else:
#     print("БД Не подгружается")
