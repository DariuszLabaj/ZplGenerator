from typing import Any, Optional


class HeadDiagnostic:
	def __init__(self, ) -> None:
		"""
		The ~HD command echoes printer status information that includes the power supply and head temperature using the terminal emulator.
		"""
pass

	def __str__(self) -> str:
		format = f"~HD"
		return format
