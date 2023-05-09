from pylibdmtx.pylibdmtx import decode
import cv2
from PIL import Image
import time

img = 'data-matrix.png'


def time_it(func):
    """ print function name + how long it took """

    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"{func.__name__} execution time: {execution_time:.2f} seconds")
        return result

    return wrapper


@time_it
def with_PIL():
    # Decode the data with PIL
    data = decode(Image.open(img))

    # Print the decoded data as string from bytes
    print(data[0].data.decode('utf-8'))


@time_it
def with_cv2():
    # Load the image with cv2
    image = cv2.imread(img, cv2.IMREAD_GRAYSCALE)

    # Decode the data
    data = decode(image)

    # Print the decoded data as string
    print(data[0].data.decode('utf-8'))


if __name__ == '__main__':
    with_PIL()
    with_cv2()
