from api import db, mashmallow

class User(db.Model):
    
    email = db.Column(db.Text, primary_key = True)
    first_name = db.Column(db.Text, nullable = False)
    last_name = db.Column(db.Text, nullable = False)
    organization_id = db.Column(db.Integer, db.ForeignKey('organization.id'), nullable = False)

    def __init__(self, email, first_name, last_name, organization_id) -> None:
        
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.organization_id = organization_id

    def __repr__(self):
        return f'<User "{self.email}">'
        

class UserSchema(mashmallow.SQLAlchemyAutoSchema):

    class Meta:
        
        model = User

user_schema = UserSchema()
users_schema = UserSchema(many=True)