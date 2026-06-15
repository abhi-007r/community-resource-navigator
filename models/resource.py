from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Text
from sqlalchemy import DateTime
from sqlalchemy.sql import func

from database.db import Base


class Resource(Base):

    __tablename__ = "resources"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    name = Column(
        String,
        nullable=False
    )

    category = Column(
        String,
        nullable=False
    )

    description = Column(
        Text,
        nullable=False
    )

    address = Column(
        String,
        nullable=True
    )

    city = Column(
        String,
        nullable=True
    )

    state = Column(
        String,
        nullable=True
    )

    phone = Column(
        String,
        nullable=True
    )

    website = Column(
        String,
        nullable=True
    )

    eligibility = Column(
        Text,
        nullable=True
    )

    services = Column(
        Text,
        nullable=True
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )