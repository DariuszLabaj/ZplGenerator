from typing import Any, Optional


class NetworkConnect:
	def __init__(self, networkIdNumber) -> None:
		"""
		The ~NC command is used to connect a particular printer to a network by calling up the printer’s network ID number
		"""
		self.__networkIdNumber = networkIdNumber

	def __str__(self) -> str:
		format = f"~NC{self.__networkIdNumber}"
		return format
