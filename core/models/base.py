from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, declared_attr


class Base(DeclarativeBase):
    __abstract__ = True

    # имя таблицы на основе названия класса
    @declared_attr
    def __tablename__(cls):
        return f"{cls.__name__.lower()}s"

    id: Mapped[int] = mapped_column(primary_key=True)
