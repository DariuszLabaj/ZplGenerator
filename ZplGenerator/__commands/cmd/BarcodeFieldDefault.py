from typing import Any, Optional


class BarcodeFieldDefault:
	def __init__(self, width, aspectRatio, height) -> None:
		"""
		The ^BY command is used to change the default values for the module width (in dots), the wide bar to narrow bar width ratio and the bar code height (in dots). It can be used as often as necessary within a label format.
		"""
		self.__width = width
		self.__aspectRatio = aspectRatio
		self.__height = height

	def __str__(self) -> str:
		format = f"^BY{self.__width},{self.__aspectRatio},{self.__height}"
		return format
