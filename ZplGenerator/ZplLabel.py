from typing import List
from ZplGenerator.ZplBoxElement import ZplBoxElement
from ZplGenerator.ZplDataMatrixElement import ZplDataMatrixElement
from ZplGenerator.ZplElement import ZplElement
from ZplGenerator.ZplGraphicElement import ZplGraphicElement
from ZplGenerator.ZplLabelConfig import ZplLabelConfig
from ZplGenerator.ZplTextElement import ZplTextElement
from ZplGenerator.fieldType import fieldType


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
        return self.__lcfg.HomeX/self.__lcfg.Dpmm, self.__lcfg.HomeY/self.__lcfg.Dpmm

    @property
    def elements(self) -> list[ZplElement]:
        return self.__label_elements

    def __init__(
            self, dpi: int = 200, label_width_mm: float = 10.0, label_height_mm: float = 10.00,
            label_darkness: int = 15, label_home_x: float = 0.0, label_home_y: float = 0.0,
            print_orientation: str = 'N', font_size: float = 5.0, font: str = "ARIAL.FMT"):
        self.__lcfg = ZplLabelConfig(
            label_width_mm, label_height_mm, label_darkness, dpi, print_orientation, label_home_x, label_home_y,
            font_size, font)
        self.__label_elements: List[ZplElement] = []
        self.__element_handle = 0
        self.__last_handle = self.__element_handle

    def getConfigurationData(self) -> str:
        command = self.SCB + '\n'
        command += str(self.__lcfg) + '\n'
        command += self.ECB
        return command

    def getLabelData(self) -> str:
        command = self.SCB + '\n'
        for element in self.__label_elements:
            if element is not None:
                command += str(element)
        command += self.ECB
        return command

    def __str__(self) -> str:
        return self.getConfigurationData()+'\n'+self.getLabelData()

    def addText(self, data, posx: float, posy: float, font=None, size=None):
        self.__last_handle = self.__element_handle
        inFont = font if font is not None else self.__lcfg.Font
        inSize = size if size is not None else self.__lcfg.FontSize
        self.__label_elements.insert(
            self.__element_handle, ZplTextElement(
                posx, posy, inSize, inFont, data, self.__lcfg.Dpmm)
        )
        self.__element_handle += 1
        return self.__last_handle

    def addDataMatrix(
            self, data: str, posx: float, posy: float, orientataion: str = 'N', symbol_height: int = 3,
            quality: int = 200, columns: int = 0, rows: int = 0, formating: int = 0):
        self.__last_handle = self.__element_handle
        self.__label_elements.insert(
            self.__element_handle, ZplDataMatrixElement(
                posx, posy, data, orientataion, symbol_height, quality, columns, rows, formating, self.__lcfg.Dpmm)
        )
        self.__element_handle += 1
        return self.__last_handle

    def addGraphicObject(
            self, posx: float = 0.0, posy: float = 0.0, source: str = 'R', data: str = 'UNKNOWN', scalex: int = 1,
            scaley: int = 1):
        self.__last_handle = self.__element_handle
        self.__label_elements.insert(
            self.__element_handle, ZplGraphicElement(
                posx, posy, source, data, scalex, scaley, self.__lcfg.Dpmm)
        )
        self.__element_handle += 1
        return self.__last_handle

    def addGraphicBox(
            self, posx: float = 0.0, posy: float = 0.0, box_width: float = 0.0, box_height: float = 0.0,
            border_thickness: float = 0.125):
        self.__last_handle = self.__element_handle
        self.__label_elements.insert(
            self.__element_handle, ZplBoxElement(
                posx, posy, box_width, box_height, border_thickness, self.__lcfg.Dpmm)
        )
        self.__element_handle += 1
        return self.__last_handle

    def editElement(
            self, handle: int, posx=None, posy=None, font=None, size=None, data=None, orientataion=None,
            symbol_height=None, symbol_quality=None, columns=None, rows=None, formating=None, source=None,
            scalex=None, scaley=None, box_width=None, box_height=None, border_thickness=None):
        __type = self.__label_elements[handle].Type
        __posx = self.__label_elements[handle].PosX if posx is None else posx
        __posy = self.__label_elements[handle].PosY if posy is None else posy
        __font = self.__label_elements[handle].Font if font is None else font
        __size = self.__label_elements[handle].FontSize if size is None else size
        __data = self.__label_elements[handle].Data if data is None else data
        __orientation = self.__label_elements[handle].Orientation if orientataion is None else orientataion
        __symbol_height = self.__label_elements[handle].SymbolHeight if symbol_height is None else symbol_height
        __symbol_quality = self.__label_elements[handle].SymbolQuality if symbol_quality is None else symbol_quality
        __columns = self.__label_elements[handle].Columns if columns is None else columns
        __rows = self.__label_elements[handle].Rows if rows is None else rows
        __formatng = self.__label_elements[handle].Formating if formating is None else formating
        __source = self.__label_elements[handle].Source if source is None else source
        __scalex = self.__label_elements[handle].ScaleX if scalex is None else scalex
        __scaley = self.__label_elements[handle].ScaleY if scaley is None else scaley
        __box_width = self.__label_elements[handle].BoxWidth if box_width is None else box_width
        __box_height = self.__label_elements[handle].BoxHeight if box_height is None else box_height
        __border_thickness = self.__label_elements[
            handle].BorderThickness if border_thickness is None else border_thickness
        match __type:
            case fieldType.text:
                self.__label_elements[handle] = ZplTextElement(
                    __posx, __posy, __size, __font, __data, self.__lcfg.Dpmm)
            case fieldType.datamatrix:
                self.__label_elements[handle] = ZplDataMatrixElement(
                    __posx, __posy, __data, __orientation, __symbol_height, __symbol_quality, __columns, __rows,
                    __formatng, self.__lcfg.Dpmm)
            case fieldType.graphic:
                self.__label_elements[handle] = ZplGraphicElement(
                    __posx, __posy, __source, __data, __scalex, __scaley, self.__lcfg.Dpmm)
            case fieldType.box:
                self.__label_elements[handle] = ZplBoxElement(
                    __posx, __posy, __box_width, __box_height, __border_thickness, self.__lcfg.Dpmm)

    def addElementsFromString(self, data: str):
        def tokenize(data: str) -> list[str]:
            data = data.replace('\n', '')
            data = data.replace('\r', '')
            data = data.replace('\t', '')
            data = data.replace('^XA', '')
            data = data.replace('^XZ', '')
            tokens = data.split('^FS')
            for token in tokens:
                token = token.strip()
            return tokens
        
        def elementize(tokens: list[str]):
            elements: list[list[str]] = []
            for token in tokens:
                if token != '':
                    elements.append(token.split('^'))
            return elements

        def createElements(strElements: list[list[str]]):
            for element in strElements:
                match element[1][:2]:
                    case 'FT':
                        positions = element[1][2:].split(',')
                        posX = int(positions[0])/self.dpmm
                        posY = int(positions[1])/self.dpmm
                        data = element[3][2:]
                        fontData = element[2].split(',')
                        font = fontData[3][2:]
                        size = int(fontData[1])/self.dpmm
                        self.addText(data, posX, posY, font, size)
                    case 'BY':
                        positions = element[2][2:].split(',')
                        posX = int(positions[0])/self.dpmm
                        posY = int(positions[1])/self.dpmm
                        data = element[4][2:]
                        dmData = element[3][2:].split(',')
                        orientataion = dmData[0]
                        symbol_height = int(dmData[1])
                        quality = int(dmData[2])
                        columns = int(dmData[3])
                        rows = int(dmData[4])
                        formating = int(dmData[5])
                        self.addDataMatrix(data, posX, posY, orientataion, symbol_height, quality, columns, rows, formating)
                    case 'FO':
                        positions = element[1][2:].split(',')
                        posX = int(positions[0])/self.dpmm
                        posY = int(positions[1])/self.dpmm
                        if element[2].startswith('GB'):
                            gbData = element[2][2:].split(',')
                            box_width = int(gbData[0])/self.dpmm
                            box_height = int(gbData[1])/self.dpmm
                            border_thickness = int(gbData[2])/self.dpmm
                            self.addGraphicBox(posX, posY, box_width, box_height, border_thickness)
        tokens = tokenize(data)
        elements = elementize(tokens)
        createElements(elements)

    def deleteElement(self, handle):
        self.__label_elements.pop(handle)

    def clearLabel(self):
        self.__label_elements = []
