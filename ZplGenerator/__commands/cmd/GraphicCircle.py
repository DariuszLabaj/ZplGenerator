from typing import Any, Optional


class GraphicCircle:
	def __init__(self, diameter, borderThickness, lineColor) -> None:
		"""
		The ^GC command produces a circle on the printed label. The command parameters specify the diameter (width) of the circle, outline thickness, and color. Thickness extends inward from the outline
		"""
		self.__diameter = diameter
		self.__borderThickness = borderThickness
		self.__lineColor = lineColor

	def __str__(self) -> str:
		format = f"^GC{self.__diameter},{self.__borderThickness},{self.__lineColor}"
		return format
