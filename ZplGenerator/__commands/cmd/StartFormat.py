from typing import Any, Optional


class StartFormat:
	def __init__(self, ) -> None:
		"""
		The ^XA command is used at the beginning of ZPL II code. It is the opening bracket and indicates the start of a new label format. This command is substituted with a single ASCII control character STX (control-B, hexadecimal 02).
		"""
pass

	def __str__(self) -> str:
		format = f"^XA"
		return format
