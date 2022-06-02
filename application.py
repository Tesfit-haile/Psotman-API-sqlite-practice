##### pip3 freeze > requirements helps for someone who use your project to have all the dependencies
##### This is a simple project for practicing postman and DB

from flask import Flask, request, json
import flask_sqlalchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///userData.db'
db = flask_sqlalchemy.SQLAlchemy(app)

##### Database



class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(30), unique=True)
    phone = db.Column(db.Integer)

    def __repr__(self):
        return f"{self.name} - {self.email} - {self.phone}"


""" 
go to terminal, write python3, import the db and the table from its file, then create_all()
Then feed the model.

>>> Important
1. db.session.add(obj)
2. db.session.commit()
>>> then you can see all the records by saying query_all().

"""


@app.route('/')
def home():
    return 'This is the Home page .....'



@app.route('/users')
def users():
    all_records = []
    # We can query this and send to the home page
    queried_records = User.query.all()  # we can send them as a list to the home page but as a JSON

    for record in queried_records:
        all_records.append({'name': record.name, 'email': record.email, 'phone': record.phone})

    return {'Users': all_records}



@app.route('/user/<id>')
def get_user_byId(id):

    user = User.query.get(id)
    obj = {'Id ': user.id, 'name': user.name, 'email': user.email, 'phone': user.phone}
    return f" The User  >>> {obj} with id >>> {id}"




@app.route('/add_user', methods=['POST', 'GET'])
def add_user():
    new_user = User(name=request.json['name'], email=request.json['email'], phone=request.json['phone'])
    db.session.add(new_user)
    db.session.commit()
    return f'Successfully... added new user to DB.... {new_user}'




@app.route('/deleteUser/<id>', methods=['DELETE'])
def deleteUser(id):
    # get the drink from the db
    userToDelete = User.query.get(id)
    if userToDelete is None: # check if it exist then delete
        return 'No such user in DB'
    db.session.delete(userToDelete)
    db.session.commit()
    return 'Success deleteUser'




@app.route('/updateUser/<id>', methods=['PUT'])
def updateUser(id):
    # get the drink from the db
    update_user = User.query.get(id)
    if update_user is None: # check if it exist then delete
        return 'No such user in DB'
    else:
        update_user.email = request.json['email']
    db.session.commit()
    ####### update user
    return 'Success updated_User'





@app.route('/deleteAllUsers', methods=['DELETE'])
def deleteAllUsers():
    # get the drink from the db
    allUsersToDelete = User.query.all()
    if len(allUsersToDelete) == 0: # check if they exist then delete
        return 'DB is empty'
    else:
        for user in allUsersToDelete:
            db.session.delete(user)
        db.session.commit()
    return 'Success deleteALLUsers'
