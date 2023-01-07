from typing import Any, Optional


class UpsMaxiCodeBarcode:
	def __init__(self, mode, symbolNumber, noOfSymbols) -> None:
		"""
		The ^BD command creates a two-dimensional, optically read (not scanned) code. This symbology was developed by UPS (United Parcel Service).
		"""
		self.__mode = mode
		self.__symbolNumber = symbolNumber
		self.__noOfSymbols = noOfSymbols

	def __str__(self) -> str:
		format = f"^BD{self.__mode},{self.__symbolNumber},{self.__noOfSymbols}"
		return format
