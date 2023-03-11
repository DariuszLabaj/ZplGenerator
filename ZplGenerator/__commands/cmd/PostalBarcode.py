from typing import Any, Optional


class PostalBarcode:
	def __init__(self, orientation, height, printInterpretationLine, printInterpretationLineAboveCode, codeType) -> None:
		"""
		The POSTAL barcode is used to automate the handling of mail. POSTAL codes use a series of tall and short bars to represent the digits.
		"""
		self.__orientation = orientation
		self.__height = height
		self.__printInterpretationLine = printInterpretationLine
		self.__printInterpretationLineAboveCode = printInterpretationLineAboveCode
		self.__codeType = codeType

	def __str__(self) -> str:
		format = f"^BZ{self.__orientation},{self.__height},{self.__printInterpretationLine},{self.__printInterpretationLineAboveCode},{self.__codeType}"
		return format
