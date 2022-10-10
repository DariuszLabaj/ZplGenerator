from typing import Protocol
from ZplGenerator.fieldType import fieldType


class ZplElement(Protocol):
    @property
    def Type(self) -> fieldType:
        ...

    @property
    def PosX(self) -> float:
        ...

    @property
    def PosY(self) -> float:
        ...

    @property
    def Font(self) -> str | None:
        ...

    @property
    def FontSize(self) -> float | None:
        ...

    @property
    def Data(self) -> str | None:
        ...

    @property
    def Orientation(self) -> str | None:
        ...

    @property
    def SymbolHeight(self) -> int | None:
        ...

    @property
    def SymbolQuality(self) -> int | None:
        ...

    @property
    def Columns(self) -> int | None:
        ...

    @property
    def Rows(self) -> int | None:
        ...

    @property
    def Formating(self) -> int | None:
        ...

    @property
    def Source(self) -> str | None:
        ...

    @property
    def ScaleX(self) -> int | None:
        ...

    @property
    def ScaleY(self) -> int | None:
        ...

    @property
    def BoxWidth(self) -> float | None:
        ...

    @property
    def BoxHeight(self) -> float | None:
        ...

    @property
    def BorderThickness(self) -> float | None:
        ...

    def __str__(self) -> str:
        ...

    def __repr__(self) -> str:
        ...
