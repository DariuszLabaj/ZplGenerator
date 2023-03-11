from typing import Any, Optional


class Code39Barcode:
	def __init__(self, orientation, mod43CheckDigit, height, printInterpretationLine, printInterpretationLineAboveCode) -> None:
		"""
		The Code 39 barcode is the standard for many industries, including the U.S. Department of Defense. It is one of three symbologies identified in the American National Standards Institute (ANSI) standard MH10.8M-1983. Code 39 is also known as USD-3 Code and 3 of 9 Code
		"""
		self.__orientation = orientation
		self.__mod43CheckDigit = mod43CheckDigit
		self.__height = height
		self.__printInterpretationLine = printInterpretationLine
		self.__printInterpretationLineAboveCode = printInterpretationLineAboveCode

	def __str__(self) -> str:
		format = f"^B3{self.__orientation},{self.__mod43CheckDigit},{self.__height},{self.__printInterpretationLine},{self.__printInterpretationLineAboveCode}"
		return format
