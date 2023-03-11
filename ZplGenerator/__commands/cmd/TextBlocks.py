from typing import Any, Optional


class TextBlocks:
	def __init__(self, blockRotation, width, height) -> None:
		"""
		The ^TB command prints a text block with defined width and height. The text block has an automatic wordwrap function. If the text exceeds the block height, the text is truncated. This command supports complex text layout features.
		"""
		self.__blockRotation = blockRotation
		self.__width = width
		self.__height = height

	def __str__(self) -> str:
		format = f"^TB{self.__blockRotation},{self.__width},{self.__height}"
		return format
