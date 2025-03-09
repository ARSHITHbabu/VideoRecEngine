from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from database import Base
import datetime

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

class Category(Base):  # ✅ Added missing Category model
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)

    videos = relationship("Video", back_populates="category")  # ✅ Bi-directional relationship with Video

class Video(Base):
    __tablename__ = "videos"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    category_id = Column(Integer, ForeignKey("categories.id"), nullable=False)
    url = Column(String)

    category = relationship("Category", back_populates="videos")  # ✅ Corrected relationship

class UserInteraction(Base):
    __tablename__ = "user_interactions"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    video_id = Column(Integer, ForeignKey("videos.id"))
    interaction_type = Column(String)  # viewed, liked, inspired, rated
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)

    user = relationship("User")
    video = relationship("Video")
