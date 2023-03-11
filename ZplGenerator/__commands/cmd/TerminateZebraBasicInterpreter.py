from typing import Any, Optional


class TerminateZebraBasicInterpreter:
	def __init__(self, ) -> None:
		"""
		The ~JQ command is used when Zebra BASIC Interpreter is active. Sending ~JQ to the printer terminates the ZBI session.
		"""
pass

	def __str__(self) -> str:
		format = f"~JQ"
		return format
