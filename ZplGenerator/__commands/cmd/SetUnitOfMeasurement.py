from typing import Any, Optional


class SetUnitOfMeasurement:
	def __init__(self, units, formatBase, desiredDotsPerInchConversion) -> None:
		"""
		The ^MU command sets the units of measurement the printer uses. ^MU works on a field-by-field basis. Once the mode of units is set, it carries over from field to field until a new mode of units is entered.
		"""
		self.__units = units
		self.__formatBase = formatBase
		self.__desiredDotsPerInchConversion = desiredDotsPerInchConversion

	def __str__(self) -> str:
		format = f"^MU{self.__units},{self.__formatBase},{self.__desiredDotsPerInchConversion}"
		return format
