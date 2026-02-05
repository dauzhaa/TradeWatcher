from fastapi import FastAPI, status

class WebSocketConnectionError(Exception):
    def __init__(self):
        super().__init__("Connection Error")
        
class WebSockerTimeError(Exception):
    def __init__(self, detail: str = "Gateway Timeout"):
        super().__init__(status_code=status.HTTP_504_GATEWAY_TIMEOUT, detail=detail)
        
    