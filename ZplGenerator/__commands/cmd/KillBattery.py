from typing import Any, Optional


class KillBattery:
	def __init__(self, ) -> None:
		"""
		The ~KB command places the printer in battery discharge mode. This allows the battery to be drained without actually printing.
		"""
pass

	def __str__(self) -> str:
		format = f"~KB"
		return format
