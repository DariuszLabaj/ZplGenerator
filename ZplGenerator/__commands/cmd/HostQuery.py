from typing import Any, Optional


class HostQuery:
	def __init__(self, type) -> None:
		"""
		The ~HQ command group causes the printer to send information back to the host
		"""
		self.__type = type

	def __str__(self) -> str:
		format = f"~HQ{self.__type}"
		return format
