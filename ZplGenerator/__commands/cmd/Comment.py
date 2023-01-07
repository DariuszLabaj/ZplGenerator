from typing import Any, Optional


class Comment:
	def __init__(self, data) -> None:
		"""
		The ^FX command is useful when you want to add non-printing informational comments or statements within a label format. Any data after the ^FX command up to the next caret (^) or tilde (~) command does not have any effect on the label format. Therefore, you should avoid using the caret (^) or tilde (~) commands within the ^FX statement.
		"""
		self.__data = data

	def __str__(self) -> str:
		format = f"^FX{self.__data}"
		return format
