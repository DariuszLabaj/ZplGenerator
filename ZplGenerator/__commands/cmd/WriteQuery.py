from typing import Any, Optional


class WriteQuery:
	def __init__(self, queryType) -> None:
		"""
		The ~WQ command triggers the printer to print a label with odometer, maintenance or alert, and printhead history information.
		"""
		self.__queryType = queryType

	def __str__(self) -> str:
		format = f"~WQ{self.__queryType}"
		return format
