from routes.convert import convertRoute


def configureRoutes(app):
    app.register_blueprint(convertRoute, url_prefix="/convert")