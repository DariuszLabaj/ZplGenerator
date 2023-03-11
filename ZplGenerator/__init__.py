from ZplGenerator.ZplLabel import ZplLabel as Label
from ZplGenerator.ZplImage import ZplImage as Image
from ZplGenerator.getGraphicsData import getGraphicsData
from ZplGenerator.getFontData import getFontData
from ZplGenerator.reverseGenerator import LabelImageGenerator


def PtTomm(points: float) -> float:
    value: float = points/72*25.4
    return value


if __name__ == '__main__':
    help(Label)
    help(Image)
    help(getGraphicsData)
    help(getFontData)
    help(LabelImageGenerator)
