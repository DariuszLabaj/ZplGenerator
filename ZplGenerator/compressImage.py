from typing import List


testResult = [
    '000000000000',  #  ,
    '000000000000',  #  :
    '000000000000',  #  :
    '000000000000',  #  :
    '000000000000',  #  :
    '000000000000',  #  :
    '000000000000',  #  :
    '000000000000',  #  :
    '000000000000',  #  :
    '000000000000',  #  :
    '800007f00002',  #  8J07FJ02
    'c0007ffc0006',  #  CI07HFCI06
    '6003fc1f800c',  #  6H03FC1F8H0C
    '300f07f1c018',  #  3H0F07F1C018
    '181800007c30',  #  1818J07C3,
    '0c1000003c60',  #  0C1K03C6,
    '063efefefcc0',  #  063EFEFEFHC,
    '031800003180',  #  0318J0318,
    '019800003300',  #  0198J0H3,
    '00d800007e00',  #  H0D8J07E,
    '006800007e00',  #  H068J07E,
    '003800007a00',  #  
    '001800007200',  #  
    '000c00006200',  #  
    '000e03f0fe00',  #  
    '000b03f1e000',  #  
    '000983f32000',  #  
    '000cc0066000',  #  
    '000c600c6000',  #  
    '000c30186000',  #  
    '000c18306000',  #  
    '000c0c604000',  #  
    '000c06c04000',  #  
    '000403804000',  #  
    '000403804000',  #  
    '000606c04000',  #  
    '00060c604000',  #  
    '00061830c000',  #  
    '00063018c000',  #  
    '0006600cc000',  #  
    '0006c006c000',  #  
    '00078003c000',  #  
    '00030001c000',  #  
    '00060001c000',  #  
    '000e0003e000',  #  
    '001b0007f000',  #  
    '0033000c3800',  #  
    '006300181c00',  #  
    '00c300199e00',  #  
    '0183ddd99b00',  #  
    '0303fff81980',  #  
    '0601800c30c0',  #  
    '0c018007e060',  #  
    '18018003c030',  #  
    '300000000018',  #  
    '60000000000c',  #  
    'c00000000006',  #  
    '800000000002',  #  
    '000000000000',  #  
    '000000000000',  #  
    '3ffffffffff8',  #  
    '3ffffffffff8',  #  
    '3ffffffffff8',  #  
    '3ffffffffff8',  #  
    '3ffffffffff8',  #  
    '3ffffffffff8',  #  
    '3ffffffffff8',  #  
    '3ffffffffff8',  #  
    '000000000000',  #  
    '000000000000',  #  
    '000000000000',  #  
    '000000000000',  #  
]


def compress(data: List[str]) -> str:
    def RepeatCount(value: int) -> str:
        repValues = [x for x in range(20, 420, 20)]
        repValues.reverse()
        temp = value
        ret = ''
        while temp > 0:
            if temp <= 0:
                break
            if temp < 20:
                ret += int.to_bytes(70+temp).decode('ASCII')
                temp -= temp
            if temp >= 20:
                for val in repValues:
                    if val <= temp:
                        ret += int.to_bytes(102+val//20).decode('ASCII')
                        temp -= val
                        break
        return ret

    def preliminaryCompress(data: str) -> str:
        currentChar = ''
        charCnt = 0
        ret = ''
        data = data.upper()
        for char in data:
            if char in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']:
                if currentChar != char:
                    if charCnt > 1:
                        ret += f"{RepeatCount(charCnt)}{currentChar}"
                        charCnt = 0
                    elif currentChar != '':
                        ret += currentChar
                        charCnt = 0
                    currentChar = char
                    charCnt += 1
                else:
                    charCnt += 1
        if charCnt > 1:
            ret += f"{RepeatCount(charCnt)}{currentChar}"
        elif currentChar != '':
            ret += currentChar
        return ret

    compressedLines = [preliminaryCompress(line) for line in data]
    simplified: List[str] = [compressedLines[0]]
    for i in range(1, len(compressedLines)):
        if compressedLines[i-1] == compressedLines[i]:
            simplified.append(':')
        else:
            simplified.append(compressedLines[i])
    for x in range(len(simplified)):
        line = simplified[x]
        if len(line) > 1:
            multiplierStop = 0
            mulStart = False
            if line[-1] == '0':
                if line[-2] not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']:
                    for i in range(len(line)):
                        if line[-(i+1)] not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F'] and not mulStart:
                            mulStart = True
                        if line[-(i+1)] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F'] and mulStart:
                            multiplierStop = -i
                            break
                    simplified[x] = line[:multiplierStop]+','
                else:
                    simplified[x] = line[:-1]+','
            elif line[-1] == 'f':
                if line[-2] not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']:
                    for i in range(len(line)):
                        if line[-(i+1)] not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F'] and not mulStart:
                            mulStart = True
                        if line[-(i+1)] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F'] and mulStart:
                            multiplierStop = -i
                            break
                    simplified[x] = line[:multiplierStop]+'!'
                else:
                    simplified[x] = line[:-1]+'!'
            # if line[-1] == '0' or line[-1] == 'f':
            #     multiplierStop = -2
            #     for i in range(len(line)):
            #         if line[-(i+1)] not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']:
            #             multiplierStop = -i-1
            #             break
            #     if line[-1] == '0':
            #         simplified[x] = line[:multiplierStop]+','
            #     else:
            #         simplified[x] = line[:multiplierStop]+'!'
    return ''.join(simplified)


if __name__ == '__main__':
    other = ',:::::::::8J07FJ02CI07FFCI066003FC1F800C300F07F1C0181818J07C3,0C1K03C6,063EFEFEFCC,0318J0318,0198J033,00D8J07E,0068J07E,0038J07A,0018J072,I0CJ062,I0E03F0FE,I0B03F1E,I0983F32,I0CC0066,I0C600C6,I0C30186,I0C18306,I0C0C604,I0C06C04,I0403804,:I0606C04,I060C604,I061830C,I063018C,I06600CC,I06C006C,I078003C,I03I01C,I06I01C,I0EI03E,001BI07F,0033I0C38,006300181C,00C300199E,0183ID99B,0303IF8198,0601800C30C,0C018007E06,18018003C03,3O0186P0CCP068P02,:3PF8:::::::,:::'
    this = compress(testResult).upper()
    for i in range(len(this)):
        print(this[i], other[i])