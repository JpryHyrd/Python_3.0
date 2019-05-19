from socket import *
import logging
import sys

logger = logging.getLogger("chat_client")
logger.setLevel(logging.DEBUG)
logger.setLevel(logging.INFO)

file_handler = logging.FileHandler("chat_client.log")
stream_handler = logging.StreamHandler(sys.stderr)

s = socket(AF_INET, SOCK_STREAM)  
s.connect(('localhost', 7777))  
msg = input("Введите сообщение серверу: ")
s.send(msg.encode('utf-8'))
data = s.recv(1000000)
print('Сообщение от сервера: ', data.decode('utf-8'))
s.close()

if __name__ == "__main__":
    logger.info("DEBUG LEVEL")
    logger.setLevel(logging.DEBUG)
    logger.debug("DEBUG log event")
    logger.info("DEBUG log event")
    logger.warning("WARNING log event")
    logger.error("ERROR log event")
    logger.critical("CRITICAL log event")

    logger.info("\nINFO LEVEL")
    logger.setLevel(logging.INFO)
    logger.debug("DEBUG log event")
    logger.info("DEBUG log event")
    logger.warning("WARNING log event")
    logger.error("ERROR log event")
    logger.critical("CRITICAL log event")

    logger.setLevel(logging.ERROR)
    logger.info("\nERROR LEVEL")
    logger.setLevel(logging.WARNING)
    logger.debug("DEBUG log event")
    logger.info("DEBUG log event")
    logger.warning("WARNING log event")
    logger.error("ERROR log event")
    logger.critical("CRITICAL log event")



