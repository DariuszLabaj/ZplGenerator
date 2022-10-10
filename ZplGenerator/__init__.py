from ZplGenerator.ZplLabel import ZplLabel as Label
from ZplGenerator.ZplImage import ZplImage as Image
from ZplGenerator.getGraphicsData import getGraphicsData
from ZplGenerator.getFontData import getFontData


def PtTomm(points: float) -> float:
    value: float = points*0.35277777777778
    return value


if __name__ == '__main__':
    help(Label)
    help(Image)
    help(getGraphicsData)
    help(getFontData)
