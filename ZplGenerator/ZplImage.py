from pathlib import Path
from typing import List, Tuple
from PIL import Image


class ZplImage():
    def __init__(self, path: Path, transparencyThreshold: int = 88, colorThreshold: int = 84, destination: str = 'R'):
        self.image = Image.open(path, 'r')
        self.destination = destination
        self.pixelData: List[Tuple[int, int, int, int]] = self.image.getdata()  # type: ignore
        self.width, self.height = self.image.size
        self.name = path.stem
        if len(self.name) > 8:
            self.name = self.name[:8]
        if not self.name.isalnum():
            raise ValueError(f"Image name must be alphanumeric, {self.name}")
        self.__black = (0, 0, 0, 255)
        self.__white = (255, 255, 255, 255)
        self.__processedData: List[Tuple[int, int, int, int]] = []
        self.__processedImage = Image.new('RGBA', self.image.size)
        self.__rawData: List[List[bool]] = []
        for i in range(self.height):
            self.__row: List[bool] = []
            for j in range(self.width):
                if isinstance(self.pixelData[i*self.width+j], tuple):  # type: ignore
                    if len(self.pixelData[i*self.width+j]) < 4:
                        self.__alpha = 255-(
                            self.pixelData[i*self.width+j][0]+self.pixelData[i*self.width+j][1] +
                            self.pixelData[i*self.width+j][2])/3
                    else:
                        self.__alpha = self.pixelData[i*self.width+j][3]
                    if self.__alpha > transparencyThreshold:
                        if (self.pixelData[i*self.width+j][0]+self.pixelData[i*self.width+j][1] +
                                self.pixelData[i*self.width+j][2])/3 > colorThreshold:
                            if (j % 2 == 0 and i % 2 == 0) or (j % 2 != 0 and i % 2 != 0):
                                self.__row.append(True)
                                self.__processedData.append(self.__black)
                            else:
                                self.__row.append(False)
                                self.__processedData.append(self.__white)
                        else:
                            self.__row.append(True)
                            self.__processedData.append(self.__black)
                    else:
                        self.__row.append(False)
                        self.__processedData.append(self.__white)
                elif isinstance(self.pixelData[i*self.width+j], int):
                    if self.pixelData[i*self.width+j] == 0:  # type: ignore
                        self.__row.append(False)
                        self.__processedData.append(self.__white)
                    else:
                        self.__row.append(True)
                        self.__processedData.append(self.__black)
            self.__rawData.append(self.__row)
        self.__numericData: List[List[int]] = []
        for row in self.__rawData:
            self.__numericRow: List[int] = []
            if len(row) % 8 != 0:
                for i in range(0, len(row)+1, 8):
                    if i < len(row):
                        self.__numericRow.append(self.BITI(8, row[i:i+8]))
                    else:
                        self.__numericRow.append(self.BITI(8, row[i:]))
            else:
                for i in range(0, len(row), 8):
                    self.__numericRow.append(self.BITI(8, row[i:i+8]))
            self.__numericData.append(self.__numericRow)
        if len(self.__processedData) == 0:
            self.__processedImage = self.image
        else:
            self.__processedImage.putdata(self.__processedData)  # type: ignore
        self.bytesRow = len(self.__numericData[0])
        self.bytesTotal = self.bytesRow*len(self.__numericData)
        self.data = ""
        for row in self.__numericData:
            for byte in row:
                self.data += f"{byte:02x}"
        self.size = self.__processedImage.size

    def BITI(self, bits: int, source: list[bool]) -> int:
        self.__dest: int = 0
        self.__temp = source
        if len(source) < bits:
            for _ in range(bits-len(source)):
                self.__temp.append(False)
        self.__temp.reverse()
        for _ in range(0, int(bits)):
            self.__dest += int(self.__temp[_])*(2**(_))
        return self.__dest

    def show(self):
        self.__processedImage.show()

    def get(self):
        return self.__processedImage

    def __str__(self) -> str:
        return f"~DG{self.destination}:{self.name}.GRF,{self.bytesTotal:05},{self.bytesRow:03},{self.data}\n"
