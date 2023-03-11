from typing import Any, Optional


class SetBatteryCondition:
	def __init__(self, pauseOnLowVoltage) -> None:
		"""
		There are two low battery voltage levels sensed by the PA/PT400™ printers. When battery voltage goes below the first level, the green LED begins flashing as a warning but printing continues. When this warning occurs, it is recommended to recharge the battery.
		"""
		self.__pauseOnLowVoltage = pauseOnLowVoltage

	def __str__(self) -> str:
		format = f"~JF{self.__pauseOnLowVoltage}"
		return format
