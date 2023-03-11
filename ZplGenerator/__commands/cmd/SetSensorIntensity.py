from typing import Any, Optional


class SetSensorIntensity:
	def __init__(self, settingToModify, value) -> None:
		"""
		The ^SI command is used to change the values for the media sensors, which are also set during the media calibration process. The media calibration process is described in your specific printer’s user’s guide.
		"""
		self.__settingToModify = settingToModify
		self.__value = value

	def __str__(self) -> str:
		format = f"^SI{self.__settingToModify},{self.__value}"
		return format
