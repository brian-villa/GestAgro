import threading
from api.api import FlaskAPI
from server.websockets import WebSocketServer

if __name__ == "__main__":
    flask_app = FlaskAPI()
    ws_server = WebSocketServer()

    flask_thread = threading.Thread(target=flask_app.run)
    ws_thread = threading.Thread(target=ws_server.run)

    flask_thread.start()
    ws_thread.start()

    flask_thread.join()
    ws_thread.join()