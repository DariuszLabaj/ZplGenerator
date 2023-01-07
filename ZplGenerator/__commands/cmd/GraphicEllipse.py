from typing import Any, Optional


class GraphicEllipse:
	def __init__(self, width, height, borderThickness, lineColor) -> None:
		"""
		The ^GE command produces an ellipse in the label format.
		"""
		self.__width = width
		self.__height = height
		self.__borderThickness = borderThickness
		self.__lineColor = lineColor

	def __str__(self) -> str:
		format = f"^GE{self.__width},{self.__height},{self.__borderThickness},{self.__lineColor}"
		return format
