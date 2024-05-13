from flask import Flask




from dotenv import load_dotenv
import os
load_dotenv()

#app factory
def create_app():
    app = Flask(__name__)
    
    #config sql database(need to create a database in postgres first)
    sql_password = os.getenv('SQL_PASSWORD')
    app.config['SQLALCHEMY_DATABASE_URI'] = sql_password
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    from .models import models
    models.db.init_app(app)
    from flask_migrate import Migrate
    migrate = Migrate(app, models.db)

    @app.route('/')
    def index():
        return 'Hello, this is Reptiles API very first index page!'
    
    from .blueprints import reptile
    app.register_blueprint(reptile.bp)


    return app