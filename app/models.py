from sqlalchemy import ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db import Base


class Cliente(Base):
    __tablename__ = "clientes"

    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(100))
    telefono: Mapped[str] = mapped_column(String(20))
    direccion: Mapped[str] = mapped_column(String(200))
    activo: Mapped[bool] = mapped_column(default=True)

    perros: Mapped[list["Perro"]] = relationship(back_populates="cliente")

    def __repr__(self) -> str:
        return f"Cliente(id={self.id!r}, nombre={self.nombre!r})"


class Perro(Base):
    __tablename__ = "perros"

    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(60))
    raza: Mapped[str | None] = mapped_column(String(60))
    tamano: Mapped[str | None] = mapped_column(String(20))
    notas: Mapped[str | None] = mapped_column(Text)
    cliente_id: Mapped[int] = mapped_column(ForeignKey("clientes.id"))
    activo: Mapped[bool] = mapped_column(default=True)

    cliente: Mapped["Cliente"] = relationship(back_populates="perros")

    def __repr__(self) -> str:
        return f"Perro(id={self.id!r}, nombre={self.nombre!r}, raza={self.raza!r})"
