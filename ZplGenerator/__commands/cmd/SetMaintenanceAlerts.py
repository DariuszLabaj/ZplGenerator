from typing import Any, Optional


class SetMaintenanceAlerts:
	def __init__(self, typeOfAlert, printLabel, printLabelThreshold, frequency, units) -> None:
		"""
		The ^MA command controls how the printer issues printed maintenance alerts. Maintenance alerts are labels that print with a warning that indicates the printhead needs to be cleaned or changed.
		"""
		self.__typeOfAlert = typeOfAlert
		self.__printLabel = printLabel
		self.__printLabelThreshold = printLabelThreshold
		self.__frequency = frequency
		self.__units = units

	def __str__(self) -> str:
		format = f"^MA{self.__typeOfAlert},{self.__}printLabel,{self.__printLabelThreshold},{self.__frequency},{self.__units}"
		return format
