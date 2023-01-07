from typing import Any, Optional


class ResetAdvancedCounters:
	def __init__(self, counterNumber) -> None:
		"""
		The ~RO command resets the advanced counters used by the printer to monitor label generation in inches, centimeters, and number of labels.
		"""
		self.__counterNumber = counterNumber

	def __str__(self) -> str:
		format = f"~RO{self.__counterNumber}"
		return format
