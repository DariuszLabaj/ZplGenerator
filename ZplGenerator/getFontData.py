from pathlib import Path
from typing import Tuple


def getFontData(fontPath: Path, destination: str = 'R') -> str:
    def __openFontFile(fontPath: Path) -> Tuple[bytes, int]:
        fontData = None
        fontSize = None
        fontData = fontPath.read_bytes()
        fontSize = len(fontData)
        return fontData, fontSize
    fontName = fontPath.name
    fontData, fontSize = __openFontFile(fontPath)
    command = f"^XA\n~DU{destination}:{fontName},{fontSize},\n"
    for byte in fontData:
        command += f"{byte:02x}"
    command += "^XZ"
    return command
