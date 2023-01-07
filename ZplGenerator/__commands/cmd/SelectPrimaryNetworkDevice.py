from typing import Any, Optional


class SelectPrimaryNetworkDevice:
	def __init__(self, primaryNetworkDevice) -> None:
		"""
		The ^NC command selects the wired or wireless print server as the primary network device
		"""
		self.__primaryNetworkDevice = primaryNetworkDevice

	def __str__(self) -> str:
		format = f"^NC{self.__primaryNetworkDevice}"
		return format
