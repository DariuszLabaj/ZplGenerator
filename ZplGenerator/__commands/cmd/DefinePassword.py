from typing import Any, Optional


class DefinePassword:
	def __init__(self, fourDigitPassword, passwordLevel) -> None:
		"""
		The ^KP command is used to define the password that must be entered to access the control panel switches and LCD Setup Mode.
		"""
		self.__fourDigitPassword = fourDigitPassword
		self.__passwordLevel = passwordLevel

	def __str__(self) -> str:
		format = f"^KP{self.__fourDigitPassword},{self.__passwordLevel}"
		return format
