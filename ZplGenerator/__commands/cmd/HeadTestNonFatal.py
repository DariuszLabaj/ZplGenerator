from typing import Any, Optional


class HeadTestNonFatal:
	def __init__(self, ) -> None:
		"""
		The ~JO command configures the printer to run the head test with error reporting enabled. When ~JO is used an error will be displayed and printing will stop if the head test fails. The user can push the PAUSE button on the printer to bypass the error. This command differs from the ~JN (Head Test Fatal) command in that a power cycle is not required in the event of a head test failure.
		"""
pass

	def __str__(self) -> str:
		format = f"~JO"
		return format
