from flask import Flask, render_template, send_from_directory

def create_app():
    app = Flask(__name__)

    # Configuración del proyecto
    app.config.from_mapping(
        DEBUG = True,
        SECRET_KEY = 'dev',
        CONNECTION_STRING = 'DRIVER={SQL Server};SERVER=IDEAPAD_CRIS;DATABASE=db_users;UID=sa;PWD=pwd_prac'
    )

    from . import auth
    app.register_blueprint(auth.bp)


    from . import products
    app.register_blueprint(products.bp)

    from . import profile
    app.register_blueprint(profile.bp)

    from . import shorcut
    app.register_blueprint(shorcut.bp)

    @app.route('/static/<path:path>')
    def send_static(path):
        return send_from_directory('static', path)

    @app.route('/')
    def index():
        return render_template('index.html')

    return app
