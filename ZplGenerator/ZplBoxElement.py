from typing import Literal
from ZplGenerator.fieldType import fieldType


class ZplBoxElement:
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
        return None

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
        return None

    @property
    def ScaleX(self) -> int | None:
        return None

    @property
    def ScaleY(self) -> int | None:
        return None

    @property
    def BoxWidth(self) -> float | None:
        return self.__boxWidth_mm

    @property
    def BoxHeight(self) -> float | None:
        return self.__boxHeight_mm

    @property
    def BorderThickness(self) -> float | None:
        return self.__borderThickness_mm

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
            self, posX_mm: float, posY_mm: float, box_width_mm: float, box_height_mm: float, border_thickness_mm: float,
            dpmm: int):
        if dpmm == 8:
            if box_width_mm < 0 or box_width_mm > 999.875:
                raise ValueError("Box width must be between 0 and 999,875 mm")
            if box_height_mm < 0 or box_height_mm > 999.875:
                raise ValueError("Box height must be between 0 and 999,875 mm")
            if border_thickness_mm < 0.125 or border_thickness_mm > 999.875:
                raise ValueError(
                    "Border thickness must be between 0.125 and 999,875 mm")
        if dpmm == 12:
            if box_width_mm < 0 or box_width_mm > 999.833:
                raise ValueError("Box width must be between 0 and 999,833 mm")
            if box_height_mm < 0 or box_height_mm > 999.833:
                raise ValueError("Box height must be between 0 and 999,833 mm")
            if border_thickness_mm < 0.125 or border_thickness_mm > 999.833:
                raise ValueError(
                    "Border thickness must be between 0.083 and 999,833 mm")
        self.__posx_mm = posX_mm
        self.__posy_mm = posY_mm
        self.__boxWidth_mm = box_width_mm
        self.__boxHeight_mm = box_height_mm
        self.__borderThickness_mm = border_thickness_mm
        self.__posx = int(posX_mm * dpmm)
        self.__posy = int(posY_mm * dpmm)
        self.__box_width = int(box_width_mm * dpmm)
        self.__box_height = int(box_height_mm * dpmm)
        self.__border_thickness = int(border_thickness_mm * dpmm)

    def __str__(self) -> str:
        return f"^FO{self.__posx},{self.__posy}^GB{self.__box_width},{self.__box_height},{self.__border_thickness}^FS\n"

    def __repr__(self) -> str:
        return self.__str__()
