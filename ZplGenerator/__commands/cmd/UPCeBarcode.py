from typing import Any, Optional


class UPCeBarcode:
	def __init__(self, orientation, height, printInterpretationLine, printInterpretationLineAboveCode, printCheckDigit) -> None:
		"""
		The ^B9 command produces a variation of the UPC symbology used for number system 0. It is a shortened version of the UPC-A barcode, where zeros are suppressed, resulting in codes that require less printing space.
		"""
		self.__orientation = orientation
		self.__height = height
		self.__printInterpretationLine = printInterpretationLine
		self.__printInterpretationLineAboveCode = printInterpretationLineAboveCode
		self.__printCheckDigit = printCheckDigit

	def __str__(self) -> str:
		format = f"^B9{self.__orientation},{self.__height},{self.__printInterpretationLine},{self.__printInterpretationLineAboveCode},{self.__printCheckDigit}"
		return format
