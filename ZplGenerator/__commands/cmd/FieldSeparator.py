from typing import Any, Optional


class FieldSeparator:
	def __init__(self, ) -> None:
		"""
		The ^FS command denotes the end of the field definition. Alternatively, ^FS command can also be issued as a single ASCII control code SI (Control-O, hexadecimal 0F).
		"""
pass

	def __str__(self) -> str:
		format = f"^FS"
		return format
