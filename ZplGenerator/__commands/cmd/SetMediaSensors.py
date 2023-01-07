from typing import Any, Optional


class SetMediaSensors:
	def __init__(self, web, media, ribbon, labelLength, intensityOfMediaLed, intensityOfRibbonLed, markSensing, markMediaSensing, markLedSensing) -> None:
		"""
		The ^SS command is used to change the values for media, web, ribbon, and label length set during the media calibration process. The media calibration process is described in your specific printer’s user’s guide.
		"""
		self.__web = web
		self.__media = media
		self.__ribbon = ribbon
		self.__labelLength = labelLength
		self.__intensityOfMediaLed = intensityOfMediaLed
		self.__intensityOfRibbonLed = intensityOfRibbonLed
		self.__markSensing = markSensing
		self.__markMediaSensing = markMediaSensing
		self.__markLedSensing = markLedSensing

	def __str__(self) -> str:
		format = f" ^SS{self.__web},{self.__media},{self.__ribbon},{self.__labelLength},{self.__intensityOfMediaLed},{self.__intensityOfRibbonLed},{self.__markSensing},{self.__markMediaSensing},{self.__markLedSensing}"
		return format
