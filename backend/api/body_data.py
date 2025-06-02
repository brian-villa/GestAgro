from threading import Lock

class BodyData:
    """
    Singleton thread para armazenar dados compartilhados no corpo da requisição,
    como localização e prioridade.

    A implementação garante que apenas uma instância de BodyData exista durante a execução,
    mesmo em ambientes multithread.

    Attributes:
        lock (threading.Lock): Lock para sincronização de acesso aos atributos da instância.
        location: Objeto que representa a localização (pode ser qualquer tipo definido no contexto).
        priority (int): Prioridade associada à requisição (padrão 0).
    """

    _instance = None  # Instância única da classe
    _lock = Lock()    # Lock para garantir thread safety na criação da instância

    def __new__(cls):
        """
        Sobrescreve a criação da instância para garantir padrão Singleton com proteção de thread.

        Returns:
            BodyData: Instância única da classe BodyData.
        """
        with cls._lock:  # Garante exclusão mútua na criação da instância
            if cls._instance is None:
                cls._instance = super(BodyData, cls).__new__(cls)
                cls._instance.lock = Lock()  # Lock para controlar acesso aos atributos da instância
                cls._instance.location = None
                cls._instance.priority = 0
            return cls._instance
