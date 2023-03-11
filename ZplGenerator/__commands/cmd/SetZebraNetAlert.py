from typing import Any, Optional


class SetZebraNetAlert:
	def __init__(self, conditionType, destinationForRouteAlert, enableConditionSetAlert, enableConditionClearAlert, destinationSetting, portNumber) -> None:
		"""
		The ^SX command is used to configure the ZebraNet Alert System.
		"""
		self.__conditionType = conditionType
		self.__destinationForRouteAlert = destinationForRouteAlert
		self.__enableConditionSetAlert = enableConditionSetAlert
		self.__enableConditionClearAlert = enableConditionClearAlert
		self.__destinationSetting = destinationSetting
		self.__portNumber = portNumber

	def __str__(self) -> str:
		format = f"^SX{self.__conditionType},{self.__destinationForRouteAlert},{self.__enableConditionSetAlert},{self.__enableConditionClearAlert},{self.__destinationSetting},{self.__portNumber}"
		return format
