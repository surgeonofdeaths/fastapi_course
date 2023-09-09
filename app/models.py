from sqlalchemy import (TIMESTAMP, Boolean, CheckConstraint, Column,
                        ForeignKey, Integer, String, text)
from sqlalchemy.orm import relationship

from .database import Base


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    published = Column(Boolean, nullable=False, server_default="TRUE")
    created_at = Column(
        TIMESTAMP(timezone=True),
        nullable=False,
        server_default=text(text="NOW()"),
    )
    owner_id = Column(
        Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False
    )
    owner = relationship("User")


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    created_at = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=text("NOW()")
    )


class Vote(Base):
    __tablename__ = "votes"

    post_id = Column(
        Integer,
        ForeignKey("posts.id", ondelete="CASCADE"),
        primary_key=True,
        nullable=False,
    )
    user_id = Column(
        Integer,
        ForeignKey("use's'id", ondelete="CASCADE"),
        primary_key=True,
        nullable=False,
    )
    vote_value = Column(
        Integer,
        CheckConstraint("vote_value=1 OR vote_value=-1"),
        server_default="1",
        nullable=False,
    )
    created_at = Column(
        TIMESTAMP(timezone=True),
        server_default=text("NOW()"),
        nullable=False,
    )
