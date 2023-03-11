

class ZplLabelConfig:
    @property
    def Width(self) -> int:
        return int(self.__width_mm * self.__dpmm)

    @property
    def Height(self) -> int:
        return int(self.__height_mm * self.__dpmm)

    @property
    def Darkness(self) -> int:
        return self.__darkness

    @property
    def Dpi(self) -> int:
        return self.__dpi

    @property
    def Dpmm(self) -> int:
        return self.__dpmm

    @property
    def Orientation(self) -> str:
        return self.__orientation

    @property
    def HomeX(self) -> int:
        return int(self.__home_x_mm * self.__dpmm)

    @property
    def HomeY(self) -> int:
        return int(self.__home_y_mm * self.__dpmm)

    @property
    def FontSize(self) -> int:
        return int(self.__font_size_mm * self.__dpmm)

    @property
    def Font(self) -> str:
        return self.__font

    def __init__(
            self, width_mm: float, height_mm: float, darkness: int, dpi: int, orientation: str, home_x: float,
            home_y: float, font_size: float, font: str):
        self.__width_mm = width_mm
        self.__height_mm = height_mm
        if darkness < 0 or darkness > 30:
            raise ValueError("Label darkness should be between 0 and 30")
        self.__darkness = darkness
        self.__dpi = dpi
        if self.__dpi == 200:
            self.__dpmm = 8
        elif self.__dpi == 300:
            self.__dpmm = 12
        else:
            raise ValueError("Allowed dpi Values are 200 and 300")
        if orientation != 'N' and orientation != 'I':
            raise ValueError(
                f"Print Orientation can be N - normal or I - inverted {orientation}")
        self.__orientation = orientation
        self.__home_x_mm = home_x
        self.__home_y_mm = home_y
        self.__font_size_mm = font_size
        self.__font = font

    def __str__(self) -> str:
        command = [
            "^JMA^PQ1,0,0,0^PRA,D,A",
            f"~SD{self.Darkness:02d}",
            "^MTT^MNY^MMT,0",
            f"^PO{self.Orientation}",
            f"^PW{self.Width}",
            "^LS0000",
            f"^ML{self.Height}",
            f"^LH{self.HomeX},{self.HomeY}",
        ]
        return '\n'.join(command)
