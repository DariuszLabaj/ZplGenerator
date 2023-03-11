from typing import Any, Optional


class SetZplMode:
	def __init__(self, version) -> None:
		"""
		The ^SZ command is used to select the programming language used by the printer. This command gives you the ability to print labels formatted in both ZPL and ZPL II.
		"""
		self.__version = version

	def __str__(self) -> str:
		format = f"^SZ{self.__version}"
		return format
