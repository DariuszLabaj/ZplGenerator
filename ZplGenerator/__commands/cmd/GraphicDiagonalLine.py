from typing import Any, Optional


class GraphicDiagonalLine:
	def __init__(self, width, height, borderThickness, lineColor, orientation) -> None:
		"""
		The ^GD command produces a straight diagonal line on a label. This can be used in conjunction with other graphic commands to create a more complex figure.
		"""
		self.__width = width
		self.__height = height
		self.__borderThickness = borderThickness
		self.__lineColor = lineColor
		self.__orientation = orientation

	def __str__(self) -> str:
		format = f"^GD{self.__width},{self.__height},{self.__borderThickness},{self.__lineColor},{self.__orientation}"
		return format
