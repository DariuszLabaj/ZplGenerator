from ZplGenerator.ZplImage import ZplImage


def getGraphicsData(*images: ZplImage) -> bytes:
    command = "^XA\n"
    for image in images:
        command += str(image)
    command += "^XZ"
    return command
