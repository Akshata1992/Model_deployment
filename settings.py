"""
--*utf-8*--
Author: Akshata
Usage: In settings.py you’ll be able to change parameters for the server connectivity, 
image dimensions + data type, and server queuing
"""
# initialize Redis connection settings
REDIS_HOST = "localhost"
REDIS_PORT = 6379
REDIS_DB = 0

#initialize all the constants for spatial dimention and datatype
IMAGE_WIDTH = 224
IMAGE_HEIGHT = 224
IMAGE_CHANS = 3
IMAGE_DTYPE = "float32"

#initialize constants used for server queuing
IMAGE_QUEUE = "image_queue"
BATCH_SIZE = 8
SERVER_SLEEP = 60
CLIENT_SLEEP = 10