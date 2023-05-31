from ZplGenerator.ZplImage import ZplImage


def getGraphicsData(*images: ZplImage) -> str:
    command = "^XA\n"
    for image in images:
        command += image.raw()
    command += "^XZ"
    return command
