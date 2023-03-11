from typing import Literal
from ZplGenerator.fieldType import fieldType


class ZplDataMatrixElement:
    @property
    def Type(self) -> fieldType:
        return fieldType.dataMatrix

    @property
    def PosX(self) -> float:
        return self.__posX_mm

    @property
    def PosY(self) -> float:
        return self.__posY_mm

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
        return self.__orientation

    @property
    def SymbolHeight(self) -> int | None:
        return self.__symbol_height

    @property
    def SymbolQuality(self) -> int | None:
        return self.__symbol_quality

    @property
    def Columns(self) -> int | None:
        return self.__columns

    @property
    def Rows(self) -> int | None:
        return self.__rows

    @property
    def Formatting(self) -> int | None:
        return self.__formatting

    @property
    def Source(self) -> str | None:
        return None

    @property
    def ScaleX(self) -> int | None:
        return None

    @property
    def ScaleY(self) -> int | None:
        return None

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

    def __init__(
            self, posX_mm: float, posY_mm: float, data: str, orientation: str, symbolHeight: int, symbolQuality: int,
            columns: int, rows: int, formatting: int, dpmm: int):
        if orientation != 'N' and orientation != 'R' and orientation != 'I' and orientation != 'B':
            raise ValueError(
                "Accepted Values:\nN = normal\nR = rotated 90 degrees(clockwise)\nI = " +
                "inverted 180 degrees\nB = read from bottom up,270 degrees ")
        if symbolQuality not in [0, 50, 80, 100, 140, 200]:
            raise ValueError("Accepted Values:0,50,80,100,140,200 ")
        if (
            (symbolQuality <= 140 and ((9 > columns or columns > 49) or columns % 2 != 1)) or
                (symbolQuality == 200 and ((10 > columns or columns > 144) or columns % 2 != 0))) and columns != 0:
            raise ValueError(
                "When ECC 0-140 is specified, the number of these values must be odd(9 - 49). And,\nwhen ECC" +
                " 200 is specified, the number of these values must be even(10, 12…, 26, 32,\n36, 40, 44, 48, " +
                "52, 64, 72, 80, 88, 96, 104, 120, 132, 144).\nMoreover, when this value is set as 0, columns " +
                f"is calculated automatically. {symbolQuality == 200},{10 > columns},{columns < 144},{columns % 2 != 0}"
            )
        if (
            (symbolQuality <= 140 and ((9 > rows or rows > 49) or rows % 2 != 1)) or
                (symbolQuality == 200 and ((10 > rows or rows > 144) or rows % 2 != 0))) and rows != 0:
            raise ValueError(
                "When ECC 0-140 is specified, the number of these values must be odd(9 - 49). And,\nwhen ECC" +
                " 200 is specified, the number of these values must be even(10, 12…, 26, 32,\n36, 40, 44, 48, " +
                "52, 64, 72, 80, 88, 96, 104, 120, 132, 144).\nMoreover, when this value is set as 0, columns " +
                "is calculated automatically.")
        if formatting not in [0, 1, 2, 3, 4, 5, 6]:
            raise ValueError(
                "Accepted Values:\n0 = Automatically choose the encodation scheme based on the characters to" +
                " be\nencoded.\n1 = Field data is numeric + space(0..9,’ ‘)\n2 = Field data is upper-case " +
                "alphanumeric + space(A..Z,’ ‘)\n3 = Field data is uppercase alphanumeric + space, period, " +
                "comma, dash, and\nslash(0..9,A..Z,”.-/”)\n4 = Field data is upper-case alphanumeric + " +
                "space(0..9,A..Z,’ ’)\n5 = Field data is full 128 ASCII 7-bit set\n6 = Field data is full 256 " +
                "ISO 8-bit set\nDefault Values: 6 ")
        self.__posX_mm = posX_mm
        self.__posY_mm = posY_mm
        self.__posX = int(posX_mm * dpmm)
        self.__posY = int(posY_mm * dpmm)
        self.__data = data
        self.__orientation = orientation
        self.__symbol_height = symbolHeight
        self.__symbol_quality = symbolQuality
        self.__columns = columns
        self.__rows = rows
        self.__formatting = formatting

    def __str__(self) -> str:
        return f"^BY2.2.10^FO{self.__posX},{self.__posY}^BX{self.__orientation},{self.__symbol_height},{self.__symbol_quality},{self.__columns},{self.__rows},{self.__formatting},^FD{self.__data}^FS\n"  # noqa: E501

    def __repr__(self) -> str:
        return self.__str__()
