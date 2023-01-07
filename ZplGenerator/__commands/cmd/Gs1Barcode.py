from typing import Any, Optional


class Gs1Barcode:
	def __init__(self, orientation, symbology, magnificationFactor, separatorHeight, height, segmentWidth) -> None:
		"""
		The ^BR command is bar code types for space-constrained identification from EAN International and the Uniform Code Council, Inc.
		"""
		self.__orientation = orientation
		self.__symbology = symbology
		self.__magnificationFactor = magnificationFactor
		self.__separatorHeight = separatorHeight
		self.__height = height
		self.__segmentWidth = segmentWidth

	def __str__(self) -> str:
		format = f"^BR{self.__orientation},{self.__symbology},{self.__magnificationFactor},{self.__separatorHeight},{self.__height},{self.__segmentWidth}"
		return format
