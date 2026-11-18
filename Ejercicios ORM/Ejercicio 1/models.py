from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey

class Base(DeclarativeBase):
    pass


class Address(Base):
    __tablename__ = "addresses"
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=True, unique=True)
    state: Mapped[str] = mapped_column(String(50))
    address: Mapped[str] = mapped_column(String(100), unique=True)
    postal_code:Mapped[int] = mapped_column()
    
    user: Mapped["User"] = relationship(back_populates="address")


class Car(Base):
    __tablename__ = "cars"
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=True)
    brand: Mapped[str] = mapped_column(String(50))
    model: Mapped[str] = mapped_column(String(100))
    year: Mapped[int] = mapped_column()
    
    user: Mapped["User"] = relationship(back_populates="car")


class User(Base):
    __tablename__ = "users"
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(50))
    email: Mapped[str] = mapped_column(String(100), unique=True)
    
    car: Mapped[list["Car"]] = relationship(back_populates="user")
    address: Mapped["Address"] = relationship(back_populates="user")
    