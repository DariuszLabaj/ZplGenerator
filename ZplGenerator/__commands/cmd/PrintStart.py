from typing import Any, Optional


class PrintStart:
	def __init__(self, ) -> None:
		"""
		The ~PS command causes a printer in Pause Mode to resume printing. The operation is identical to pressing PAUSE on the control panel of the printer when the printer is already in Pause Mode.
		"""
pass

	def __str__(self) -> str:
		format = f"~PS"
		return format
