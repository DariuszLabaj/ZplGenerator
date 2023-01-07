from typing import Any, Optional


class TearOffAdjustPosition:
	def __init__(self, value) -> None:
		"""
		The ~TA command lets you adjust the rest position of the media after a label is printed, which changes the position at which the label is torn or cut.
		"""
		self.__value = value

	def __str__(self) -> str:
		format = f"~TA{self.__value}"
		return format
