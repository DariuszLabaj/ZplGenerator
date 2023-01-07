from typing import Any, Optional


class PowerOnReset:
	def __init__(self, ) -> None:
		"""
		The ~JR command resets all of the printer’s internal software, performs a power-on self-test (POST), clears the buffer and DRAM, and resets communication parameters and default values. Issuing a ~JR command performs the same function as a manual power-on reset.
		"""
pass

	def __str__(self) -> str:
		format = f"~JR"
		return format
