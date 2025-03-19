from flask import Flask, render_template

# Routes
from app.routes import  IndexRoutes

app = Flask(__name__, template_folder="templates")


def init_app(config):
    # Configuration
    app.config.from_object(config)

    # Blueprints
    app.register_blueprint(IndexRoutes.main, url_prefix='/')

    # Global error handlers
    
    @app.errorhandler(404)
    def page_not_found(error):
        return render_template('pages/404.html'), 404

    @app.errorhandler(500)
    def internal_server_error(error):
        return render_template('pages/500.html'), 500

    @app.errorhandler(503)
    def service_unavailable(error):
        return render_template('pages/503.html'), 503
    
   
    return app