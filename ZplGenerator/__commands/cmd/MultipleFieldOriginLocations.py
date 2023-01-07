from typing import Any, Optional


class MultipleFieldOriginLocations:
	def __init__(self, xPositions, yPositions) -> None:
		"""
		The ^FM command allows you to control the placement of bar code symbols.
		"""
		self.__xPositions = xPositions
		self.__yPositions = yPositions

	def __str__(self) -> str:
		format = f"^FMx1,y1,x2,y2,..."
		return format
