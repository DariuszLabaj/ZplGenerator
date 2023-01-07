from typing import Any, Optional


class EndFormat:
	def __init__(self, ) -> None:
		"""
		The ^XZ command is the ending (closing) bracket. It indicates the end of a label format. When this command is received, a label prints. This command can also be issued as a single ASCII control character ETX (Control-C, hexadecimal 03).
		"""
pass

	def __str__(self) -> str:
		format = f"^XZ"
		return format
