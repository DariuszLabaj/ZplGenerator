from typing import Any, Optional


class SetDynamicMediaCalibration:
	def __init__(self, dynamicLengthCalibration, dynamicThresholdCalibration, dynamicGainCalibration) -> None:
		"""
		The ^XS command controls whether dynamic media calibration is performed to compensate for variations in label length, position, transmissivity, and/or reflectance after a printer is powered-up or the printer has been opened (for example to change or check the media).
		"""
		self.__dynamicLengthCalibration = dynamicLengthCalibration
		self.__dynamicThresholdCalibration = dynamicThresholdCalibration
		self.__dynamicGainCalibration = dynamicGainCalibration

	def __str__(self) -> str:
		format = f"^XS{self.__dynamicLengthCalibration},{self.__dynamicThresholdCalibration}"
		return format
