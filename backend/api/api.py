from flask import Flask
from flask_cors import CORS
from controllers.ForecastController import forecast_flask
from controllers.LocationController import location_flask

class FlaskAPI:
    """
    Classe para configuração e inicialização da aplicação Flask com CORS e Blueprints.

    Attributes:
        app (Flask): Instância da aplicação Flask.
    """

    def __init__(self):
        """
        Inicializa a aplicação Flask, habilita CORS e registra os Blueprints de rotas.
        """
        self.app = Flask(__name__)
        CORS(self.app)  # Permite requisições Cross-Origin
        self.app.register_blueprint(forecast_flask)  # Rota /forecast
        self.app.register_blueprint(location_flask)  # Rota /location
    
    def run(self):
        """
        Executa a aplicação Flask.

        Args:
            debug (bool): Habilita modo debug para facilitar desenvolvimento.
            use_reloader (bool): Evita execução múltipla durante reload automático.
            port (int): Porta em que a aplicação será executada.
        """
        self.app.run(debug=True, use_reloader=False, port=5000)
