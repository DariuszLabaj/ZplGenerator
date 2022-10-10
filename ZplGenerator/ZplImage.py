from pathlib import Path
from PIL import Image


class ZplImage():
    def __init__(self, path: Path, tansparency_treshold: int = 88, colour_treshold: int = 84, destination: str = 'R'):
        self.image = Image.open(path, 'r')
        self.destination = destination
        self.pixeldata = self.image.getdata()
        self.width, self.height = self.image.size
        self.name = path.stem
        if len(self.name) > 8:
            self.name = self.name[:8]
        if not self.name.isalnum():
            raise ValueError(f"Image name must be alphanumeric, {self.name}")
        self.__black = (0, 0, 0, 255)
        self.__white = (255, 255, 255, 255)
        self.__processeddata = []
        self.__processedimage = Image.new('RGBA', self.image.size)
        self.__rawdata = []
        for i in range(self.height):
            self.__row = []
            for j in range(self.width):
                if isinstance(self.pixeldata[i*self.width+j], tuple):
                    if len(self.pixeldata[i*self.width+j]) < 4:
                        self.__alpha = 255-(
                            self.pixeldata[i*self.width+j][0]+self.pixeldata[i*self.width+j][1] +
                            self.pixeldata[i*self.width+j][2])/3
                    else:
                        self.__alpha = self.pixeldata[i*self.width+j][3]
                    if self.__alpha > tansparency_treshold:
                        if (self.pixeldata[i*self.width+j][0]+self.pixeldata[i*self.width+j][1] +
                                self.pixeldata[i*self.width+j][2])/3 > colour_treshold:
                            if (j % 2 == 0 and i % 2 == 0) or (j % 2 != 0 and i % 2 != 0):
                                self.__row.append(True)
                                self.__processeddata.append(self.__black)
                            else:
                                self.__row.append(False)
                                self.__processeddata.append(self.__white)
                        else:
                            self.__row.append(True)
                            self.__processeddata.append(self.__black)
                    else:
                        self.__row.append(False)
                        self.__processeddata.append(self.__white)
                elif isinstance(self.pixeldata[i*self.width+j], int):
                    if self.pixeldata[i*self.width+j] == 0:
                        self.__row.append(False)
                        self.__processeddata.append(self.__white)
                    else:
                        self.__row.append(True)
                        self.__processeddata.append(self.__black)
            self.__rawdata.append(self.__row)
        self.__numericdata = []
        for row in self.__rawdata:
            self.__numericrow = []
            if len(row) % 8 != 0:
                for i in range(0, len(row)+1, 8):
                    if i < len(row):
                        self.__numericrow.append(self.BITI(8, row[i:i+8]))
                    else:
                        self.__numericrow.append(self.BITI(8, row[i:]))
            else:
                for i in range(0, len(row), 8):
                    self.__numericrow.append(self.BITI(8, row[i:i+8]))
            self.__numericdata.append(self.__numericrow)
        if len(self.__processeddata) == 0:
            self.__processedimage = self.image
        else:
            self.__processedimage.putdata(self.__processeddata)
        self.bytesRow = len(self.__numericdata[0])
        self.bytesTotal = self.bytesRow*len(self.__numericdata)
        self.data = ""
        for row in self.__numericdata:
            for byte in row:
                self.data += f"{byte:02x}"
        self.size = self.__processedimage.size

    def BITI(self, bits, source: list):
        self.__dest = 0
        self.__temp = source
        if len(source) < bits:
            for _ in range(bits-len(source)):
                self.__temp.append(False)
        self.__temp.reverse()
        for _ in range(0, int(bits)):
            self.__dest += int(self.__temp[_])*(2**(_))
        return self.__dest

    def show(self):
        self.__processedimage.show()

    def get(self):
        return self.__processedimage

    def __str__(self) -> str:
        return f"~DG{self.destination}:{self.name}.GRF,{self.bytesTotal:05},{self.bytesRow:03},{self.data}\n"
