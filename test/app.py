from flask import Flask, request, jsonify
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)


#User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False,unique=True)

    def to_dict(self):
        return {"id":self.id,"name":self.name,"email":self.email}

#Create database
with app.app_context():
    db.create_all()


class UserResource(Resource):
    def post(self):
        data = request.get_json()
        new_user = User(name=data['name'],email=data['email'])
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"message":"User Created Successfully","user":{"id": new_user.id
                                                                      ,"name":new_user.name}})


class UserListResource(Resource):
    def get(self):
        users = User.query.all()
        return jsonify([user.to_dict() for user in users])
#API routes
api.add_resource(UserResource,"/users")           #POST
api.add_resource(UserListResource,"/users")       #GET

admin = Admin(app,name="User Database",template_mode="bootstrap3")
admin.add_view(ModelView(User,db.session))


if __name__ == '__main__':
    app.run(debug=True)