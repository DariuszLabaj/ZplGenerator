from typing import Any, Optional


class SlewToHomePosition:
	def __init__(self, ) -> None:
		"""
		The ~PH command feeds one label after the format currently being printed is done or when the printer is placed in pause.
		"""
pass

	def __str__(self) -> str:
		format = f"~PH"
		return format
