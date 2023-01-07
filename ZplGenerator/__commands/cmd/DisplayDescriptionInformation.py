from typing import Any, Optional


class DisplayDescriptionInformation:
	def __init__(self, descriptionToReturn) -> None:
		"""
		The ^HZ command is used for returning printer description information in XML format. The printer returns information on format parameters, object directories, individual object data, and print status information.
		"""
		self.__descriptionToReturn = descriptionToReturn

	def __str__(self) -> str:
		format = f"^HZ{self.__descriptionToReturn}"
		return format
