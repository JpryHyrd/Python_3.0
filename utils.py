from datetime import datetime

HTTP_RESPONSE_OK = "OK"

response_dict = {
    HTTP_RESPONSE_OK:{
        "response": 200,
    },
    "Bad Request": {
        "response": 400,
        "error": 'Bad Request'
    }
}

presence_d = {
    "action" : "presence",
    "time" : datetime.now().isoformat(),
    "type": "status",
    "user": {
        "account_name": "test",
        "status": "I'm here"
    }
}

receive_size = 1000





