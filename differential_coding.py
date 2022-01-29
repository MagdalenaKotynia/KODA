import numpy as np
from statistics import median

NO_PREDICTION = 0
PREDICTION_LEFT = 1
PREDICTION_UP = 2
PREDICTION_MED = 3


class DifferentialEncoder:

    @staticmethod
    def encode(image, predictionMode = PREDICTION_LEFT):

        if image is None:
            raise ValueError("Image is None.")

        if image.ndim != 2:
            raise ValueError("Invalid image shape! Pixels have to be scalars.")

        _image = np.copy(image)
        offset = 127

        if predictionMode == PREDICTION_LEFT:
            col = np.repeat(offset, _image.shape[0])
            prediction = np.column_stack((col,_image[:,:-1]))
        elif predictionMode == PREDICTION_UP:
            row = np.repeat(offset, _image.shape[1])
            prediction = np.row_stack((row,_image[:-1,:]))
        elif predictionMode == PREDICTION_MED:
            col = np.repeat(offset, _image.shape[0])
            left = np.column_stack((col,_image[:,:-1]))

            row = np.repeat(offset, _image.shape[1])
            up = np.row_stack((row,_image[:-1,:]))

            row = np.repeat(offset, _image.shape[1] - 1)
            leftUp = np.column_stack((col, np.row_stack((row, _image[:-1,:-1]))))

            allNeighbors = np.dstack((left, up, leftUp))
            prediction = np.median(allNeighbors, axis=2)
        else:
            raise ValueError("Invalid prediction mode!")

        return (_image - prediction).astype(np.int16)

    @staticmethod
    def decode(differentialImage, predictionMode = PREDICTION_LEFT):

        if differentialImage is None:
            raise ValueError("DifferentialImage is None.")

        image = np.copy(differentialImage)
        offset = 127

        if image.ndim != 2:
            raise ValueError("Invalid differential image shape! Pixels have to be scalars.")

        if predictionMode == PREDICTION_LEFT:
            image[:,0] += offset

            for x in range(1, image.shape[1]):
                image[:,x] += image[:,x - 1]
        elif predictionMode == PREDICTION_UP:
            image[0,:] +=  offset

            for y in range(1, image.shape[0]):
                image[y,:] += image[y - 1,:]
        elif predictionMode == PREDICTION_MED:
            image[0,:] +=  offset
            image[1:,0] +=  offset

            for x in range(1, image.shape[1]):
                for y in range(1, image.shape[0]):
                    image[y,x] += median([image[y - 1,x - 1],image[y - 1,x],image[y,x - 1]])
        else:
            raise ValueError("Invalid prediction mode!")

        return image.astype(np.uint8)