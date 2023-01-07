from typing import Any, Optional


class SetDarkness:
	def __init__(self, desiredDarknessSetting) -> None:
		"""
		The ~SD command allows you to set the darkness of printing. ~SD is the equivalent of the darkness setting parameter on the control panel display
		"""
		self.__desiredDarknessSetting = desiredDarknessSetting

	def __str__(self) -> str:
		format = f"~SD{self.__desiredDarknessSetting}"
		return format
