from typing import Any, Optional


class BatteryStatus:
	def __init__(self, ) -> None:
		"""
		When the ~HB command is sent to the printer, a data string is sent back to the host. The string starts with an <STX> control code sequence and terminates by an <ETX><CR><LF> control code sequence.
		"""
pass

	def __str__(self) -> str:
		format = f"~HB"
		return format
