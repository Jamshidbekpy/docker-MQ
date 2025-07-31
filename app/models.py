from sqlalchemy import Integer, String, ForeignKey, Date, func, Boolean
from sqlalchemy.orm import relationship, declarative_base, Mapped, mapped_column

Base = declarative_base()

class TimestampMixin:
    created_at: Mapped[Date] = mapped_column(Date, default=func.now())
    updated_at : Mapped[Date] = mapped_column(Date, default=func.now(), onupdate=func.now())
    
    
class User(Base, TimestampMixin):
    __tablename__ = "users"

    id : Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    username : Mapped[str] = mapped_column(String, unique=True, index=True, nullable=True)
    email : Mapped[str] = mapped_column(String, unique=True, index=True, nullable=True)
    hashed_password : Mapped[str] = mapped_column(String, nullable=True)
    is_active : Mapped[bool] = mapped_column(Boolean, default=True)

    tasks = relationship("Task", back_populates="owner")


class Task(Base, TimestampMixin):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String, index=True)
    description: Mapped[str] = mapped_column(String, index=True)
    priority: Mapped[int] = mapped_column(Integer)
    due_date: Mapped[Date] = mapped_column(Date)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))

    owner = relationship("User", back_populates="tasks")

__all__= ["Base", "User", "Task"]