from typing import Any, Optional


class CodeValidation:
	def __init__(self, codeValidation) -> None:
		"""
		The ^CV command acts as a switch to turn the code validation function on and off. When this command is turned on, all bar code data is checked for these error conditions:
Code Validation
• character not in character set
• check-digit incorrect
• data field too long (too many characters)
• data field too short (too few characters)
• parameter string contains incorrect data or missing parameter
		"""
		self.__codeValidation = codeValidation

	def __str__(self) -> str:
		format = f"^CV{self.__codeValidation}"
		return format
