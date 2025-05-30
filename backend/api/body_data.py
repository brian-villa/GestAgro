from threading import Lock

class BodyData:
    _instance = None
    _lock = Lock()

    def __new__(cls):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super(BodyData, cls). __new__(cls)
                cls._instance.lock = Lock()
                cls._instance.location = None
                cls._instance.priority = 0
            return cls._instance
