from typing import Any, Optional


class NetworkIdNumber:
	def __init__(self, networkIdNumberAssigned) -> None:
		"""
		The ^NI command is used to assign a network ID number to the printer. This must be done before the printer can be used in a network
		"""
		self.__networkIdNumberAssigned = networkIdNumberAssigned

	def __str__(self) -> str:
		format = f"^NI{self.__networkIdNumberAssigned}"
		return format
