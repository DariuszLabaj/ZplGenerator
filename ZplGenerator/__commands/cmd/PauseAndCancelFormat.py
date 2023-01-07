from typing import Any, Optional


class PauseAndCancelFormat:
	def __init__(self, ) -> None:
		"""
		The ~JP command clears the format currently being processed and places the printer into Pause Mode.
		"""
pass

	def __str__(self) -> str:
		format = f"~JP"
		return format
