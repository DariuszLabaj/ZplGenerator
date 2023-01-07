from typing import Any, Optional


class MaximumLabelLength:
	def __init__(self, length) -> None:
		"""
		The ^ML command lets you adjust the maximum label length.
		"""
		self.__length = length

	def __str__(self) -> str:
		format = f"^ML{self.__length}"
		return format
