from typing import Any, Optional


class StartPrint:
	def __init__(self, dotRowToStartPrinting) -> None:
		"""
		The ^SP command allows a label to start printing at a specified point before the entire label has been completely formatted. On extremely complex labels, this command can increase the overall throughput of the print.
		"""
		self.__dotRowToStartPrinting = dotRowToStartPrinting

	def __str__(self) -> str:
		format = f"^SP{self.__StartPrint}"
		return format
