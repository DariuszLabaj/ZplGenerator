from typing import Any, Optional


class AztecBarcodeParameters:
	def __init__(self, orientation, magnificationFactor, eccicIndicator, errorControl, menuSymbolIndicator, noOfSymbols, idFiled: Optional[Any]) -> None:
		"""
		The ^BO command creates a two-dimensional matrix symbology made up of square modules arranged around a bulls-eye pattern at the center.
		"""
		self.__orientation = orientation
		self.__magnificationFactor = magnificationFactor
		self.__eccicIndicator = eccicIndicator
		self.__errorControl = errorControl
		self.__menuSymbolIndicator = menuSymbolIndicator
		self.__noOfSymbols = noOfSymbols
		self.__idFiled = idFiled if idFiled else ''

	def __str__(self) -> str:
		format = f"^BO{self.__orientation},{self.__magnificationFactor},{self.__eccicIndicator},{self.__errorControl},{self.__menuSymbolIndicator},{self.__noOfSymbols},{self.__idFiled}"
		return format
