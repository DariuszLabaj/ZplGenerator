from typing import Any, Optional


class DataMatrixBarcode:
	def __init__(self, orientation, height, qualityLevel, noOfColumns, noOfRows, formatID, escapeSequenceCharacter, aspectRatio) -> None:
		"""
		The ^BX command creates a two-dimensional matrix symbology made up of square modules arranged within a perimeter finder pattern.
		"""
		self.__orientation = orientation
		self.__height = height
		self.__qualityLevel = qualityLevel
		self.__noOfColumns = noOfColumns
		self.__noOfRows = noOfRows
		self.__formatID = formatID
		self.__escapeSequenceCharacter = escapeSequenceCharacter
		self.__aspectRatio = aspectRatio

	def __str__(self) -> str:
		format = f"^BX{self.__orientation},{self.__height},{self.__qualityLevel},{self.__noOfColumns},{self.__noOfRows},{self.__formatID},{self.__escapeSequenceCharacter},{self.__aspectRatio}"
		return format
