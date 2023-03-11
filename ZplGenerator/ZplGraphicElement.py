from typing import Literal
from ZplGenerator.fieldType import fieldType


class ZplGraphicElement:
    @property
    def Type(self) -> fieldType:
        return fieldType.text

    @property
    def PosX(self) -> float:
        return self.__posx_mm

    @property
    def PosY(self) -> float:
        return self.__posy_mm

    @property
    def Font(self) -> str | None:
        return None

    @property
    def FontSize(self) -> float | None:
        return None

    @property
    def Data(self) -> str | None:
        return self.__data

    @property
    def Orientation(self) -> str | None:
        return None

    @property
    def SymbolHeight(self) -> int | None:
        return None

    @property
    def SymbolQuality(self) -> int | None:
        return None

    @property
    def Columns(self) -> int | None:
        return None

    @property
    def Rows(self) -> int | None:
        return None

    @property
    def Formating(self) -> int | None:
        return None

    @property
    def Source(self) -> str | None:
        return self.__source

    @property
    def ScaleX(self) -> int | None:
        return self.__scaleX

    @property
    def ScaleY(self) -> int | None:
        return self.__scaleY

    @property
    def BoxWidth(self) -> float | None:
        return None

    @property
    def BoxHeight(self) -> float | None:
        return None

    @property
    def BorderThickness(self) -> float | None:
        return None

    @property
    def MaxNumberOfLines(self) -> int | None:
        return None

    @property
    def SpaceBetweenLines(self) -> int | None:
        return None

    @property
    def TextJustified(self) -> Literal['L', 'C', 'R', 'J'] | None:
        return None

    def __init__(self, posX_mm: float, posY_mm: float, source: str, data: str, scaleX: int, scaleY: int, dpmm: int):
        if not source.isalnum() or len(source) > 8:
            raise ValueError(
                "Source Accepted Values: up to 8 alphanumeric characters")
        if not data.isalnum() or len(data) > 8:
            raise ValueError(
                "Name Accepted Values: up to 8 alphanumeric characters", data)
        if 1 > scaleX or scaleX > 10:
            raise ValueError("Scale x Accepted Values: 1 to 10")
        if 1 > scaleY or scaleY > 10:
            raise ValueError("Scale y Accepted Values: 1 to 10")
        self.__posx_mm = posX_mm
        self.__posy_mm = posY_mm
        self.__source = source
        self.__data = data
        self.__scaleX = scaleX
        self.__scaleY = scaleY
        self.__posx = int(posX_mm * dpmm)
        self.__posy = int(posY_mm * dpmm)

    def __str__(self) -> str:
        return f"^FO{self.__posx},{self.__posy}^XG{self.__source}:{self.__data}.GRF,{self.__scaleX},{self.__scaleY}^FS\n"  # noqa: E501

    def __repr__(self) -> str:
        return self.__str__()
