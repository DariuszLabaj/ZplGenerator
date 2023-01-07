from typing import Any, Optional


class ProgramablePause:
	def __init__(self, ) -> None:
		"""
		The ~PP command stops printing after the current label is complete (if one is printing) and places the printer in Pause Mode.
		"""
pass

	def __str__(self) -> str:
		format = f"~PP"
		return format
