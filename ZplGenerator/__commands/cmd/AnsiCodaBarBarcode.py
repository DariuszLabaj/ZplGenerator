from typing import Any, Optional


class AnsiCodaBarBarcode:
	def __init__(self, orientation, checkDigit, height, printInterpretationLine, printInterpretationLineAboveCode, startCharacter, stopCharacter) -> None:
		"""
		The ANSI Codabar bar code is used in a variety of information processing applications such as libraries, the medical industry, and overnight package delivery companies. This bar code is also known as USD-4 code, NW-7, and 2 of 7 code. It was originally developed for retail price labeling.
		"""
		self.__orientation = orientation
		self.__checkDigit = checkDigit
		self.__height = height
		self.__printInterpretationLine = printInterpretationLine
		self.__printInterpretationLineAboveCode = printInterpretationLineAboveCode
		self.__startCharacter = startCharacter
		self.__stopCharacter = stopCharacter

	def __str__(self) -> str:
		format = f"^BK{self.__orientation},{self.__checkDigit},{self.__height},{self.__printInterpretationLine},{self.__printInterpretationLineAboveCode},{self.__startCharacter},{self.__stopCharacter}"
		return format
