from typing import Literal, Optional
from ZplGenerator.fieldType import fieldType


class ZplTextElement:
    __printerFonts = [
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'GS', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', '0'
    ]

    @property
    def Type(self) -> fieldType:
        return fieldType.text

    @property
    def PosX(self) -> float:
        return self.__posX_mm

    @property
    def PosY(self) -> float:
        return self.__posY_mm

    @property
    def Font(self) -> str | None:
        return self.__font

    @property
    def FontSize(self) -> float | None:
        return self.__fontSize_mm

    @property
    def Data(self) -> str | None:
        return self.__data

    @property
    def Orientation(self) -> str | None:
        return self.__orientation

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
    def Formatting(self) -> int | None:
        return None

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
        return self.__Width_mm

    @property
    def BoxHeight(self) -> float | None:
        return None

    @property
    def BorderThickness(self) -> float | None:
        return None

    @property
    def MaxNumberOfLines(self) -> int | None:
        return self.__maxNumberOfLines

    @property
    def SpaceBetweenLines(self) -> int | None:
        return self.__spaceBetweenLines

    @property
    def TextJustified(self) -> Literal['L', 'C', 'R', 'J'] | None:
        return self.__justify

    def __init__(
            self, posX_mm: float, posY_mm: float, fontSize: float, font: str, data: str, dpmm: int,
            maxNumberOfLines: int, spaceBetweenLines: int, width: Optional[float] = None,
            justify: Optional[Literal['Left', 'Center', 'Right', 'Justified']] = None,
            orientation: Literal['Normal', 'Rotated', 'Inverted', 'BottomUp'] = 'Normal') -> None:
        self.__posX_mm = posX_mm
        self.__posY_mm = posY_mm
        self.__fontSize_mm = fontSize
        self.__font = font
        self.__data = data
        self.__posx = int(posX_mm * dpmm)
        self.__posy = round(posY_mm * dpmm)
        self.__size = int(fontSize * dpmm)
        self.__maxNumberOfLines = maxNumberOfLines
        self.__spaceBetweenLines = spaceBetweenLines
        self.__Width_mm = width
        self.__width = int(width * dpmm) if width is not None else None
        self.__justify: Literal['L', 'C', 'R', 'J'] | None = justify[0] if justify is not None else None  # type: ignore
        self.__orientation = orientation[0]

    def __justifiedFont(self) -> str:
        if self.__width is None or self.__justify is None:
            return self.__simpleText()
        font = f'^A{self.__font}{self.__orientation},{self.__size},' if self.__font in self.__printerFonts else f'^A@{self.__orientation},{self.__size},,B:{self.__font}'  # noqa: E501
        return f"^FO{self.__posx},{self.__posy},{font}^FB{self.__width},{self.__maxNumberOfLines},{self.__spaceBetweenLines},{self.__justify},0^FD{self.__data}^FS\n"  # noqa: E501

    def __simpleText(self) -> str:
        font = f'^A{self.__font}{self.__orientation},{self.__size},' if self.__font in self.__printerFonts else f'^A@{self.__orientation},{self.__size},,B:{self.__font}'  # noqa: E501
        return f"^FT{self.__posx},{self.__posy},{font}^FD{self.__data}^FS\n"  # noqa: E501

    def __str__(self) -> str:
        return self.__justifiedFont()

    def __repr__(self) -> str:
        return self.__str__()
