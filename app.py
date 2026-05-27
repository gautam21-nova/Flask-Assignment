from db.userdbcontext import Base
from utils.settings import engine
from flask import Flask
from controllers.usercontrol import user_bp

# building a flask builder for apis
app = Flask(__name__)

#middleware for establishing our controllers
app.register_blueprint(user_bp)

#to create databse or related table if not created it will create it
Base.metadata.create_all(bind=engine)

#entry point
if __name__ == '__main__':
    app.run(debug=True)
