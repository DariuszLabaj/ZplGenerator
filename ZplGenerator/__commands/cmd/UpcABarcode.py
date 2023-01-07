from typing import Any, Optional


class UpcABarcode:
	def __init__(self, orientation, height, printInterpretationLine, printInterpretationLineAboveCode, checkDigit) -> None:
		"""
		The ^BU command produces a fixed length, numeric symbology. It is primarily used in the retail industry for labeling packages. The UPC-A bar code has 11 data characters. The 6 dot/mm, 12 dot/mm, and 24 dot/mm printheads produce the UPC-A bar code (UPC/EAN symbologies) at 100 percent size. However, an 8 dot/ mm printhead produces the UPC/EAN symbologies at a magnification factor of 77 percent.
		"""
		self.__orientation = orientation
		self.__height = height
		self.__printInterpretationLine = printInterpretationLine
		self.__printInterpretationLineAboveCode = printInterpretationLineAboveCode
		self.__checkDigit = checkDigit

	def __str__(self) -> str:
		format = f"^BU{self.__orientation},{self.__height},{self.__printInterpretationLine},{self.__printInterpretationLineAboveCode},{self.__checkDigit}"
		return format
