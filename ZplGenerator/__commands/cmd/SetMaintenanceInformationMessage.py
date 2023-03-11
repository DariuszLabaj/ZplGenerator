from typing import Any, Optional


class SetMaintenanceInformationMessage:
	def __init__(self, alertType, message) -> None:
		"""
		The ^MI command controls the content of maintenance alert messages, which are reminders printed by the printer to instruct the operator to clean or replace the printhead.
		"""
		self.__alertType = alertType
		self.__message = message

	def __str__(self) -> str:
		format = f"^MI{self.__alertType},{self.__message}"
		return format
