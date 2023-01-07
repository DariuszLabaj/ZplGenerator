from typing import Any, Optional


class ConfigurationLabelReturn:
	def __init__(self, ) -> None:
		"""
		The ^HH command echoes printer configuration back to the host, using a terminal emulator
		"""
pass

	def __str__(self) -> str:
		format = f"^HH"
		return format
