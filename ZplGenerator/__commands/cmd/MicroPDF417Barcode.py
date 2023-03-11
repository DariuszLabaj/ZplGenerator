from typing import Any, Optional


class MicroPDF417Barcode:
	def __init__(self, orientation, height, mode) -> None:
		"""
		The ^BF command creates a two-dimensional, multi-row, continuous, stacked symbology identical to PDF417, except it replaces the 17-module-wide start and stop patterns and left/right row indicators with a unique set of 10-module-wide row address patterns. These reduce overall symbol width and allow linear scanning at row heights as low as 2X.
		"""
		self.__orientation = orientation
		self.__height = height
		self.__mode = mode

	def __str__(self) -> str:
		format = f"^BF{self.__orientation},{self.__height},{self.__mode}"
		return format
