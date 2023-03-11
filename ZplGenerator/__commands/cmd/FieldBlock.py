from typing import Any, Optional


class FieldBlock:
	def __init__(self, width, maxNoOfLinesInBlock, spaceBetweenLines, justification, indent) -> None:
		"""
		The ^FB command allows you to print text into a defined block type format. This command formats an ^FD or ^SN string into a block of text using the origin, font, and rotation specified for the text string. The ^FB command also contains an automatic word-wrap function.
		"""
		self.__width = width
		self.__maxNoOfLinesInBlock = maxNoOfLinesInBlock
		self.__spaceBetweenLines = spaceBetweenLines
		self.__justification = justification
		self.__indent = indent

	def __str__(self) -> str:
		format = f"^FB{self.__width},{self.__maxNoOfLinesInBlock},{self.__spaceBetweenLines},{self.__justification},{self.__indent}"
		return format
