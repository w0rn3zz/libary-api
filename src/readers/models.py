from datetime import datetime
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database import Base


class Reader(Base):
    __tablename__ = "readers"
    
    email: Mapped[str] = mapped_column(nullable=False, unique=True)
    name: Mapped[str] = mapped_column(unique=True, nullable=False)