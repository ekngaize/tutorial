from sqlalchemy import select, String, DateTime, Float
from sqlalchemy.orm import mapped_column, Mapped, DeclarativeBase


class Base(DeclarativeBase):
    pass


class MesureL3(Base):
    __tablename__ = "mesure_l3"
    __table_args__ = {"schema": "egms"}

    probe_id: Mapped[str] = mapped_column(String, primary_key=True)
    timestamp: Mapped[DateTime] = mapped_column(DateTime, primary_key=True)
    value: Mapped[float] = mapped_column(Float)

    @classmethod
    def get_query(cls, pid_list):
        return select(cls).where(cls.probe_id.in_(pid_list))
