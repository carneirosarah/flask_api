from api import db, mashmallow

class Organization(db.Model):

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.Text, nullable = False)
    users = db.relationship('User', backref='organization', lazy=True)

    def __init__(self, name) -> None:
        
        self.name = name

    def __repr__(self):
        return f'<Organization "{self.name}">'
        

class OrganizationSchema(mashmallow.SQLAlchemyAutoSchema):

    class Meta:
        
        model = Organization

organization_schema = OrganizationSchema()
organizations_schema = OrganizationSchema(many=True)
