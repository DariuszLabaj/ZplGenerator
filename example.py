from pathlib import Path

import ZplGenerator as Zpl


def main():
    # Creating Font File to send
    fontData = Zpl.getFontData(Path(".\\Example\\OSansBold.ttf"))
    zplFontFile = Path(".\\Example\\OSansBold.zpl")
    with zplFontFile.open("w", encoding="ASCII") as file:
        file.write(fontData)
    # Creating Image File to send
    zplImage = Zpl.Image(Path(".\\Example\\settings_FILL1.png"), destination="E")
    zplImageFile = Path(f".\\Example\\{zplImage.name}.zpl")
    zplImageData = Zpl.getGraphicsData(zplImage)
    with zplImageFile.open("w", encoding="ASCII") as file:
        file.write(zplImageData)
    # Creating Label
    label = Zpl.Label(
        dpi=300,
        label_width_mm=120,
        label_height_mm=50,
        label_darkness=0,
        label_home_x=0.5,
        label_home_y=0.5,
        print_orientation="N",
        font_size=Zpl.PtTo_mm(4),
        font="OSansBold.TTF",
    )
    # Adding objects to label
    # Text Objects
    objText1 = label.addText(data='Text1', posx=10,
                             posy=20, size=Zpl.PtTo_mm(8))
    label.addText(data='Text2', posx=30, posy=20)  # noqa: F841
    # Graphic Object
    label.addGraphicObject(  # noqa: F841
        pos_x=0.85, pos_y=2.0, source="E", data=zplImage.name
    )
    # Graphic Box Object
    label.addGraphicBox(  # noqa: F841
        pos_x=60, pos_y=20, box_width=20, box_height=30, border_thickness=0.25
    )
    # DataMatrix Object
    label.addDataMatrix(
        data="Test1234", pos_x=85, pos_y=10, symbol_height=4, columns=40, rows=40
    )  # noqa: F841
    # Editing Object
    label.editElement(objText1, data="Text456")
    # Creating printer configuration file to send
    zplConfigFile = Path(".\\Example\\printerCfg.zpl")
    zplConfigData = label.getConfigurationData()
    with zplConfigFile.open("w", encoding="ASCII") as file:
        file.write(zplConfigData)
    # Creating Label File to send
    zplLabelFile = Path(".\\Example\\label.zpl")
    zplLabelData = label.getLabelData()
    with zplLabelFile.open("w", encoding="ASCII") as file:
        file.write(zplLabelData)

    print(label)


if __name__ == "__main__":
    main()
