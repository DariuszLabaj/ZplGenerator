from ZplGenerator.fieldType import fieldType


class ZplTextElement:
    @property
    def Type(self) -> fieldType:
        return fieldType.text

    @property
    def PosX(self) -> float:
        return self.__pos_x_mm

    @property
    def PosY(self) -> float:
        return self.__pos_y_mm

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
        return None

    @property
    def BoxHeight(self) -> float | None:
        return None

    @property
    def BorderThickness(self) -> float | None:
        return None

    def __init__(self, posX_mm: float, posY_mm: float, fontSize: float, font: str, data: str, dpmm: int):
        self.__pos_x_mm = posX_mm
        self.__pos_y_mm = posY_mm
        self.__fontSize_mm = fontSize
        self.__font = font
        self.__data = data
        self.__pos_x = int(posX_mm * dpmm)
        self.__pos_y = int(posY_mm * dpmm)
        self.__size = int(fontSize * dpmm)

    def __str__(self) -> str:
        return f"^FT{self.__pos_x},{self.__pos_y},^A@N,{self.__size},,B:{self.__font}^FD{self.__data}^FS\n"

    def __repr__(self) -> str:
        return self.__str__()
