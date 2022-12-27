from ZplGenerator.ZplBoxElement import ZplBoxElement
from ZplGenerator.ZplTextElement import ZplTextElement
from PIL import Image, ImageDraw, ImageFont
from ZplGenerator.ZplDataMatrixElement import ZplDataMatrixElement
from ZplGenerator.ZplLabel import ZplLabel
from pylibdmtx.pylibdmtx import encode as dmEncode


class ZplLabelImageGenerator:

    @staticmethod
    def GenerateImage(label: ZplLabel) -> None:
        img = Image.new('RGB', (int(label.width), int(label.height)), color='white')
        img.info['dpi'] = (300, 300)
        draw = ImageDraw.Draw(img)
        for element in label.elements:
            if (isinstance(element, ZplTextElement)):
                if element.FontSize is None or element.Data is None:
                    raise Exception
                size = int(element.FontSize*label.dpmm)
                fnt = ImageFont.truetype(element.Font, size)
                draw.text(
                    (int(element.PosX*label.dpmm),
                     int(element.PosY*label.dpmm-size)),
                    element.Data,
                    font=fnt,
                    fill=(0, 0, 0)
                )
            elif (isinstance(element, ZplBoxElement)):
                if element.BoxWidth is None or element.BoxHeight is None or element.BorderThickness is None:
                    raise Exception()
                x1 = element.PosX*label.dpmm
                y1 = element.PosY*label.dpmm
                x2 = int(x1+element.BoxWidth*label.dpmm)
                y2 = int(y1+element.BoxHeight*label.dpmm)
                draw.rectangle(
                    xy=((x1, y1), (x2, y2)),
                    outline='#000000',
                    width=int(element.BorderThickness*label.dpmm)
                )
            elif (isinstance(element, ZplDataMatrixElement)):
                encoded_data = dmEncode(element.Data.encode(
                    'ascii'), size=f'{element.Columns}x{element.Rows}')
                barcode_img = Image.frombytes("RGB", (encoded_data.width, encoded_data.height),
                                              encoded_data.pixels)
                img.paste(barcode_img, (int(element.PosX*label.dpmm),
                          int(element.PosY*label.dpmm)))

        img.save('test.png')


def prepareData(data: str) -> str:
    data = data.replace('<text1>', '123456')
    data = data.replace('<text2>', '1234-ABC1234')
    data = data.replace('<text3>', 'A')
    data = data.replace('<text4>', 'Abcde 12345 !@#$%')
    data = data.replace('<text5>', '220613')
    data = data.replace('<text6>', '1')
    data = data.replace('<text7>', '12345')
    return data


def main() -> None:
    """
    SSL Cer
    """
    sampleData = """^XA
^FT36,156,^A@N,50,,B:ARIALNB.TTF^FD<text1>^FS
^FT36,216,^A@N,50,,B:ARIALNB.TTF^FD<text2>^FS
^FT430,216,^A@N,50,,B:ARIALNB.TTF^FD<text3>^FS
^FT36,276,^A@N,38,,B:ARIALNB.TTF^FD<text4>^FS
^FT36,330,^A@N,38,,B:ARIALNB.TTF^FDAbcde 12345 !@#$%^FS
^FT50,382,^A@N,29,,B:ARIALNB.TTF^FD<text5>^FS
^FT80,427,^A@N,29,,B:ARIALNB.TTF^FD<text6>^FS
^FT156,414,^A@N,50,,B:ARIALNB.TTF^FD<text7>^FS
^BY2.2.10^FO750,252^BXN,5,200,32,32,0,^FD<text2>;<text3>;<text5>;<text6>;<text7>^FS
^FO141,348^GB144,93,3^FS
^FO36,393^GB108,48,3^FS
^FO36,348^GB108,48,3^FS^XZ"""
    label = ZplLabel(dpi=300, label_width_mm=80, label_height_mm=40)
    label.addElementsFromString(prepareData(sampleData))
    ZplLabelImageGenerator.GenerateImage(label)


if __name__ == '__main__':
    main()
