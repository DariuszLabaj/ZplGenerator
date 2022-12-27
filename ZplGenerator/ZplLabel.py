from typing import List

from ZplGenerator.fieldType import fieldType
from ZplGenerator.ZplBoxElement import ZplBoxElement
from ZplGenerator.ZplDataMatrixElement import ZplDataMatrixElement
from ZplGenerator.ZplElement import ZplElement
from ZplGenerator.ZplGraphicElement import ZplGraphicElement
from ZplGenerator.ZplLabelConfig import ZplLabelConfig
from ZplGenerator.ZplTextElement import ZplTextElement


class ZplLabel:
    SCB: str = "^XA"
    ECB: str = "^XZ"

    @property
    def dpmm(self) -> int:
        return self.__lcfg.Dpmm

    @property
    def width(self) -> float:
        return self.__lcfg.Width

    @property
    def height(self) -> float:
        return self.__lcfg.Height

    @property
    def homePosition(self) -> tuple[float, float]:
        return (
            self.__lcfg.HomeX / self.__lcfg.Dpmm,
            self.__lcfg.HomeY / self.__lcfg.Dpmm,
        )

    @property
    def elements(self) -> list[ZplElement]:
        return self.__label_elements

    def __init__(
        self,
        dpi: int = 200,
        label_width_mm: float = 10.0,
        label_height_mm: float = 10.00,
        label_darkness: int = 15,
        label_home_x: float = 0.0,
        label_home_y: float = 0.0,
        print_orientation: str = "N",
        font_size: float = 5.0,
        font: str = "ARIAL.FMT",
    ):
        self.__lcfg = ZplLabelConfig(
            label_width_mm,
            label_height_mm,
            label_darkness,
            dpi,
            print_orientation,
            label_home_x,
            label_home_y,
            font_size,
            font,
        )
        self.__label_elements: List[ZplElement] = []
        self.__element_handle = 0
        self.__last_handle = self.__element_handle

    def getConfigurationData(self) -> str:
        command = self.SCB + "\n"
        command += str(self.__lcfg) + "\n"
        command += self.ECB
        return command

    def getLabelData(self) -> str:
        command = self.SCB + "\n"
        for element in self.__label_elements:
            if element is not None:
                command += str(element)
        command += self.ECB
        return command

    def __str__(self) -> str:
        return self.getConfigurationData() + "\n" + self.getLabelData()

    def addText(
        self,
        data: str,
        pos_x: float,
        pos_y: float,
        font: str | None = None,
        size: float | None = None,
    ):
        self.__last_handle = self.__element_handle
        inFont = font if font is not None else self.__lcfg.Font
        inSize = size if size is not None else self.__lcfg.FontSize
        self.__label_elements.insert(
            self.__element_handle,
            ZplTextElement(pos_x, pos_y, inSize, inFont, data, self.__lcfg.Dpmm),
        )
        self.__element_handle += 1
        return self.__last_handle

    def addDataMatrix(
        self,
        data: str,
        pos_x: float,
        pos_y: float,
        orientation: str = "N",
        symbol_height: int = 3,
        quality: int = 200,
        columns: int = 0,
        rows: int = 0,
        formatting: int = 0,
    ):
        self.__last_handle = self.__element_handle
        self.__label_elements.insert(
            self.__element_handle,
            ZplDataMatrixElement(
                pos_x,
                pos_y,
                data,
                orientation,
                symbol_height,
                quality,
                columns,
                rows,
                formatting,
                self.__lcfg.Dpmm,
            ),
        )
        self.__element_handle += 1
        return self.__last_handle

    def addGraphicObject(
        self,
        pos_x: float = 0.0,
        pos_y: float = 0.0,
        source: str = "R",
        data: str = "UNKNOWN",
        scale_x: int = 1,
        scale_y: int = 1,
    ):
        self.__last_handle = self.__element_handle
        self.__label_elements.insert(
            self.__element_handle,
            ZplGraphicElement(
                pos_x, pos_y, source, data, scale_x, scale_y, self.__lcfg.Dpmm
            ),
        )
        self.__element_handle += 1
        return self.__last_handle

    def addGraphicBox(
        self,
        pos_x: float = 0.0,
        pos_y: float = 0.0,
        box_width: float = 0.0,
        box_height: float = 0.0,
        border_thickness: float = 0.125,
    ):
        self.__last_handle = self.__element_handle
        self.__label_elements.insert(
            self.__element_handle,
            ZplBoxElement(
                pos_x, pos_y, box_width, box_height, border_thickness, self.__lcfg.Dpmm
            ),
        )
        self.__element_handle += 1
        return self.__last_handle

    def editElement(
        self,
        handle: int,
        pos_x: float | None = None,
        pos_y: float | None = None,
        font: str | None = None,
        size: float | None = None,
        data: str | None = None,
        orientation: str | None = None,
        symbol_height: int | None = None,
        symbol_quality: int | None = None,
        columns: int | None = None,
        rows: int | None = None,
        formatting: int | None = None,
        source: str | None = None,
        scale_x: int | None = None,
        scale_y: int | None = None,
        box_width: float | None = None,
        box_height: float | None = None,
        border_thickness: float | None = None,
    ):
        __type = self.__label_elements[handle].Type
        __pos_x = self.__label_elements[handle].PosX if pos_x is None else pos_x
        __pos_y = self.__label_elements[handle].PosY if pos_y is None else pos_y
        __font = self.__label_elements[handle].Font if font is None else font
        __font = __font if __font is not None else ""
        __size = self.__label_elements[handle].FontSize if size is None else size
        __size = __size if __size is not None else 0.0
        __data = self.__label_elements[handle].Data if data is None else data
        __data = __data if __data is not None else ""
        __orientation = (
            self.__label_elements[handle].Orientation
            if orientation is None
            else orientation
        )
        __orientation = __orientation if __orientation is not None else ""
        __symbol_height = (
            self.__label_elements[handle].SymbolHeight
            if symbol_height is None
            else symbol_height
        )
        __symbol_height = __symbol_height if __symbol_height is not None else 0
        __symbol_quality = (
            self.__label_elements[handle].SymbolQuality
            if symbol_quality is None
            else symbol_quality
        )
        __symbol_quality = __symbol_quality if __symbol_quality is not None else 0
        __columns = (
            self.__label_elements[handle].Columns if columns is None else columns
        )
        __columns = __columns if __columns is not None else 0
        __rows = self.__label_elements[handle].Rows if rows is None else rows
        __rows = __rows if __rows is not None else 0
        __formatting = (
            self.__label_elements[handle].Formatting
            if formatting is None
            else formatting
        )
        __formatting = __formatting if __formatting is not None else 0
        __source = self.__label_elements[handle].Source if source is None else source
        __source = __source if __source is not None else ""
        __scale_x = self.__label_elements[handle].ScaleX if scale_x is None else scale_x
        __scale_x = __scale_x if __scale_x is not None else 0
        __scale_y = self.__label_elements[handle].ScaleY if scale_y is None else scale_y
        __scale_y = __scale_y if __scale_y is not None else 0
        __box_width = (
            self.__label_elements[handle].BoxWidth if box_width is None else box_width
        )
        __box_width = __box_width if __box_width is not None else 0.0
        __box_height = (
            self.__label_elements[handle].BoxHeight
            if box_height is None
            else box_height
        )
        __box_height = __box_height if __box_height is not None else 0.0
        __border_thickness = (
            self.__label_elements[handle].BorderThickness
            if border_thickness is None
            else border_thickness
        )
        __border_thickness = (
            __border_thickness if __border_thickness is not None else 0.0
        )
        match __type:
            case fieldType.text:
                self.__label_elements[handle] = ZplTextElement(
                    __pos_x, __pos_y, __size, __font, __data, self.__lcfg.Dpmm
                )
            case fieldType.dataMatrix:
                self.__label_elements[handle] = ZplDataMatrixElement(
                    __pos_x,
                    __pos_y,
                    __data,
                    __orientation,
                    __symbol_height,
                    __symbol_quality,
                    __columns,
                    __rows,
                    __formatting,
                    self.__lcfg.Dpmm,
                )
            case fieldType.graphic:
                self.__label_elements[handle] = ZplGraphicElement(
                    __pos_x,
                    __pos_y,
                    __source,
                    __data,
                    __scale_x,
                    __scale_y,
                    self.__lcfg.Dpmm,
                )
            case fieldType.box:
                self.__label_elements[handle] = ZplBoxElement(
                    __pos_x,
                    __pos_y,
                    __box_width,
                    __box_height,
                    __border_thickness,
                    self.__lcfg.Dpmm,
                )

    def addElementsFromString(self, data: str):
        def tokenize(data: str) -> list[str]:
            data = data.replace("\n", "")
            data = data.replace("\r", "")
            data = data.replace("\t", "")
            data = data.replace("^XA", "")
            data = data.replace("^XZ", "")
            tokens = data.split("^FS")
            for token in tokens:
                token = token.strip()
            return tokens

        def processTokensToElements(tokens: list[str]):
            elements: list[list[str]] = []
            for token in tokens:
                if token:
                    elements.append(token.split("^"))
            return elements

        def createElements(strElements: list[list[str]]):
            for element in strElements:
                match element[1][:2]:
                    case "FT":
                        positions = element[1][2:].split(",")
                        posX = int(positions[0]) / self.dpmm
                        posY = int(positions[1]) / self.dpmm
                        data = element[3][2:]
                        fontData = element[2].split(",")
                        font = fontData[3][2:]
                        size = int(fontData[1]) / self.dpmm
                        self.addText(data, posX, posY, font, size)
                    case "BY":
                        positions = element[2][2:].split(",")
                        posX = int(positions[0]) / self.dpmm
                        posY = int(positions[1]) / self.dpmm
                        data = element[4][2:]
                        dmData = element[3][2:].split(",")
                        orientation = dmData[0]
                        symbol_height = int(dmData[1])
                        quality = int(dmData[2])
                        columns = int(dmData[3])
                        rows = int(dmData[4])
                        formatting = int(dmData[5])
                        self.addDataMatrix(
                            data,
                            posX,
                            posY,
                            orientation,
                            symbol_height,
                            quality,
                            columns,
                            rows,
                            formatting,
                        )
                    case "FO":
                        positions = element[1][2:].split(",")
                        posX = int(positions[0]) / self.dpmm
                        posY = int(positions[1]) / self.dpmm
                        if element[2].startswith("GB"):
                            gbData = element[2][2:].split(",")
                            box_width = int(gbData[0]) / self.dpmm
                            box_height = int(gbData[1]) / self.dpmm
                            border_thickness = int(gbData[2]) / self.dpmm
                            self.addGraphicBox(
                                posX, posY, box_width, box_height, border_thickness
                            )
                    case _:
                        pass

        tokens = tokenize(data)
        elements = processTokensToElements(tokens)
        createElements(elements)

    def deleteElement(self, handle: int):
        self.__label_elements.pop(handle)

    def clearLabel(self):
        self.__label_elements = []
