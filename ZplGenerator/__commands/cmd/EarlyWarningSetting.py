from typing import Any, Optional


class EarlyWarningSetting:
	def __init__(self, earlyWarningMedia, labelsPerRoll, mediaReplaced, ribbonLength, ribbonReplaced, earlyWarningMaintenance, headCleaningInterval, headClean, headLifeThreshold, headReplaced) -> None:
		"""
		The ^JH command configures the early warning messages that appear on the LCD.
		"""
		self.__earlyWarningMedia = earlyWarningMedia
		self.__labelsPerRoll = labelsPerRoll
		self.__mediaReplaced = mediaReplaced
		self.__ribbonLength = ribbonLength
		self.__ribbonReplaced = ribbonReplaced
		self.__earlyWarningMaintenance = earlyWarningMaintenance
		self.__headCleaningInterval = headCleaningInterval
		self.__headClean = headClean
		self.__headLifeThreshold = headLifeThreshold
		self.__headReplaced = headReplaced

	def __str__(self) -> str:
		format = f"^JH{self.__earlyWarningMedia},{self.__labelsPerRoll},{self.__mediaReplaced},{self.__ribbonLength},{self.__ribbonReplaced},{self.__earlyWarningMaintenance},{self.__headCleaningInterval},{self.__headClean},{self.__headLifeThreshold},{self.__headReplaced}"
		return format
