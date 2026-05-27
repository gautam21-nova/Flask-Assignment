from flask import Blueprint,render_template, request
from db.userdbcontext import User
from utils.settings import engine
from sqlalchemy.orm import sessionmaker

# creating a session to connect with our database
SessionLocal = sessionmaker(bind=engine)

#making blueprint for our controllers to register futher in main file
user_bp = Blueprint("user_bp", __name__)


@user_bp.route("/", methods=["GET"])
def index():
    return "Welcome to User API"


#get request for hello word
@user_bp.route("/hello",methods=["GET"])
def hello():
    return render_template("home.html")

#get request for user data retrieving
@user_bp.route("/users", methods=["GET"])
def get():
    with SessionLocal() as session:
        all_user = session.query(User).all()
        return render_template("index.html", users=all_user)
    # if conenction got cancelled or not found any record
    return "Invalid credentials", 401


#getting a user with id as params passed in url
@user_bp.route("/users/<int:id>", methods=["GET"])
def get_user(id):
    with SessionLocal() as session:
        user = session.query(User).filter(User.id == id).first()
        if user:
            return render_template("user.html", user=user)
        else:
            #error message
            return "User not found", 404


# adding user in database
@user_bp.route("/new_user",methods=["GET","POST"])
def post():

    if request.method == "POST":
        with SessionLocal() as session:
            name = request.form.get("name")
            email = request.form.get("email")
            role = request.form.get("role")
            new_user = User(name=name,email=email,role=role)
            user = session.query(User).filter(User.email==new_user.email).first()
            # checking is user already exists or not
            if(user):
                return "User alredy existed", 409
            session.add(new_user)
            session.commit()

            # successfully added message
            return "User created successfully",200

    return render_template("newuser.html")