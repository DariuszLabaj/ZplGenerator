from typing import Any, Optional


class ModeProtection:
	def __init__(self, modeToProtect) -> None:
		"""
		The ^MP command is used to disable the various mode functions on the control panel. Once disabled, the settings for the particular mode function can no longer be changed and the LED associated with the function does not light.
		"""
		self.__modeToProtect = modeToProtect

	def __str__(self) -> str:
		format = f"^MP{self.__modeToProtect}"
		return format
