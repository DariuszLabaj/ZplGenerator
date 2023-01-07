from typing import Any, Optional


class SensorSelect:
	def __init__(self, sensorSelection) -> None:
		"""
		
		"""
		self.__sensorSelection = sensorSelection

	def __str__(self) -> str:
		format = f"^JS{self.__sensorSelection}"
		return format
