from socket import *
import time
import logging
import sys

logger = logging.getLogger("chat_server")
logger.setLevel(logging.DEBUG)
logger.setLevel(logging.INFO)

file_handler = logging.FileHandler("chat_server.log")
stream_handler = logging.StreamHandler(sys.stderr)


s = socket(AF_INET, SOCK_STREAM) 
s.bind(('', 7777))               
s.listen(5)                       
                                                               
while True:
    client, addr = s.accept()
    data = client.recv(1000000)
    print('Сообщение: ', data.decode('utf-8'), ',\nОтправлено клиентом: ', addr)
    msg = 'Привет, клиент'
    client.send(msg.encode('utf-8'))
    client.close()

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






