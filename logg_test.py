import logging

logger = logging.getLogger("Simple")
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler("app.log")
logger.addHandler(file_handler)

logger.info("This is an info message")
logger.error("this is and error message")

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
age = 23
logging.info("The value of age is %d",age)


logger.debug("This is debug")
logger.info("This is info")
logger.warning("This is warning")
logger.error("This is error")
logger.critical("This is critical")

logging.basicConfig(level=logging.DEBUG,format='%(levelname)s: %(message)s')
def fun(val):
    if val<0:
        raise ValueError("Invalid Value")
    else:
        logging.info("Operation Success")

try:
    val=-1
    fun(val)
except ValueError as ve:
    logging.exception("Exception occurred %s",str(ve))