from typing import Any, Optional


class HostStatusReturn:
	def __init__(self, ) -> None:
		"""
		When the host sends ~HS to the printer, the printer sends three data strings back. Each string starts with an <STX> control code and is terminated by an <ETX><CR><LF> control code sequence. To avoid confusion, the host prints each string on a separate line.
		"""
pass

	def __str__(self) -> str:
		format = f"~HS"
		return format
