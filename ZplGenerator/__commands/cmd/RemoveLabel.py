from typing import Any, Optional


class RemoveLabel:
	def __init__(self, mode) -> None:
		"""
		The ^CP command causes the printer to move a printed label out of the presenter area in one of several ways.
		"""
		self.__mode = mode

	def __str__(self) -> str:
		format = f"^CP{self.__mode}"
		return format
