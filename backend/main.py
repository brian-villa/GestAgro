import threading
from api.api import FlaskAPI
from server.websockets import WebSocketServer

def main():
    """
    Função principal para executar a aplicação Flask e o servidor WebSocket em threads paralelas.

    Cria instâncias da API Flask e do servidor WebSocket, executando cada uma em uma thread
    separada para permitir a execução simultânea dos dois servidores.

    As threads são iniciadas e o programa espera que ambas terminem (o que normalmente não ocorre,
    pois ambos os servidores são contínuos).

    Returns:
        None
    """
    flask_app = FlaskAPI()
    ws_server = WebSocketServer()

    flask_thread = threading.Thread(target=flask_app.run)
    ws_thread = threading.Thread(target=ws_server.run)

    flask_thread.start()
    ws_thread.start()

    flask_thread.join()
    ws_thread.join()


if __name__ == "__main__":
    main()
