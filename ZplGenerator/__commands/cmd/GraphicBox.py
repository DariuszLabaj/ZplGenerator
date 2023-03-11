from typing import Any, Optional


class GraphicBox:
	def __init__(self, width, height, borderThickness, lineColor, cornerRadius) -> None:
		"""
		The ^GB command is used to draw boxes and lines as part of a label format. Boxes and lines are used to highlight important information, divide labels into distinct areas, or to improve the appearance of a label. The same format command is used for drawing either boxes or lines.
		"""
		self.__width = width
		self.__height = height
		self.__borderThickness = borderThickness
		self.__lineColor = lineColor
		self.__cornerRadius = cornerRadius

	def __str__(self) -> str:
		format = f"^GB{self.__width},{self.__height},{self.__borderThickness},{self.__lineColor},{self.__cornerRadius}"
		return format
