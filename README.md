# Zpl language command generator for generating labels, fonts and graphic files to send to printers using Zpl language

## Creating Font File

```py
fontData = Zpl.getFontData(Path('.\\Example\\OSansBold.ttf'))
zplFontFile = Path('.\\Example\\OSansBold.zpl')
with zplFontFile.open('w', encoding='ASCII') as file:
    file.write(fontData)
```

## Creating Image file

```py
zplImage = Zpl.Image(
    Path('.\\Example\\settings_FILL1.png'), destination='E')
zplImageFile = Path(f'.\\Example\\{zplImage.name}.zpl')
zplImageData = Zpl.getGraphicsData(zplImage)
with zplImageFile.open('w', encoding='ASCII') as file:
    file.write(zplImageData)
```

## Creating Label

```py
label = Zpl.Label(
    dpi=300,
    label_width_mm=120,
    label_height_mm=50,
    label_darkness=0,
    label_home_x=0.5,
    label_home_y=0.5,
    print_orientation='N',
    font_size=Zpl.PtTomm(4),
    font='OSansBold.TTF')
```

### Adding objects To label

- Text Object

```py
objText1 = label.addText(data='Text1', posx=10,
                            posy=20, size=Zpl.PtTomm(8))
objText2 = label.addText(data='Text2', posx=30, posy=20)
```

- Graphic Objects

```py
objImage = label.addGraphicObject(
    posx=0.85, posy=2.0, source='E', data=zplImage.name)
```

- Graphic Box Objects

```py
objBox = label.addGraphicBox(
    posx=60, posy=20, box_width=20, box_height=30, border_thickness=0.25)
```

- Datamatrix Objects

```py
objDm = label.addDataMatrix(data='Test1234', posx=85, posy=10, symbol_height=4, columns=40, rows=40)
```

### Editing Objects

```py
label.editElement(objText1, data='Text456')
```

### Creating printer configuration

```py
zplConfigFile = Path('.\\Example\\printerCfg.zpl')
zplConfigData = label.getConfigurationData()
with zplConfigFile.open('w', encoding='ASCII') as file:
    file.write(zplConfigData)
```

### Saving Label

```py
zplLabelFile = Path('.\\Example\\label.zpl')
zplLabelData = label.getLabelData()
with zplLabelFile.open('w', encoding='ASCII') as file:
    file.write(zplLabelData)
```
