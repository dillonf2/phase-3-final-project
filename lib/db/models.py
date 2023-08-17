from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Game(Base):
    __tablename__ = 'games'

    id = Column(Integer, primary_key=True)
    participants = relationship("Participant", back_populates="game", cascade="all, delete-orphan")
    high_scores = relationship("HighScore", back_populates="game", cascade="all, delete-orphan")
    max_range = Column(Integer)
    number_to_guess = Column(Integer)
    winner = Column(String)
    winning_percentage = Column(Float)

class Participant(Base):
    __tablename__ = 'participants'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    guess = Column(Integer)
    game_id = Column(Integer, ForeignKey('games.id'))
    game = relationship("Game", back_populates="participants")

class HighScore(Base):
    __tablename__ = 'high_scores'

    id = Column(Integer, primary_key=True)
    game_id = Column(Integer, ForeignKey('games.id'))
    participant = Column(String)
    max_range = Column(Integer)
    number_to_guess = Column(Integer)
    guess = Column(Integer)
    guess_accuracy = Column(Float)
    game = relationship("Game", back_populates="high_scores")

engine = create_engine('sqlite:///mydatabase.db')
Session = sessionmaker(bind=engine)
Base.metadata.create_all(engine)