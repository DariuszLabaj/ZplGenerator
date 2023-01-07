from typing import Any, Optional


class StartZBI:
	def __init__(self, ) -> None:
		"""
		~JI works much like the ^JI command. Both commands are sent to the printer to initialize the Zebra BASIC Interpreter
		"""
pass

	def __str__(self) -> str:
		format = f"~JI"
		return format
