from api import *

@app.route("/organization/")
def list_organizations():

    try:
  
        organizations = Organization.query.all()
        return jsonify(organizations_schema.dump(organizations))

    except Exception as e:

        logging.error("List Organizations: " +  str(e.__class__) + " :" + str(e))
        return "Sorry, couldn't retrieve the organizations.", 500

@app.route("/organization/<int:organization_id>/")
def get_organization(organization_id):

    try:

        organization = Organization.query.get(organization_id)

        return organization_schema.jsonify(organization)

    except Exception as e:

        logging.error("Get Organizations: " +  str(e.__class__) + " :" + str(e))
        return "Sorry, couldn't retrieve the organization.", 500

@app.route("/organization/users/<int:organization_id>/")
def get_organization_users(organization_id):
    
    try:

        organization = Organization.query.get(organization_id)

        if organization:
            
            for user in organization.users:
                
                user.email = user.email + '@' + organization.name + '.com'
            
            return jsonify(users_schema.dump(organization.users))
        
        else:

            return 'Please, pass a valid organization id.', 400

    except Exception as e:

        logging.error("Get Organization Users: " +  str(e.__class__) + " :" + str(e))
        return "Sorry, couldn't retrieve the users employed by this organization.", 500

@app.route("/organization/", methods=['POST'])
def create_organization():

    try:
    
        name = request.json.get('name', '')

        if len(name) > 0:

            organization = Organization(name)
            
            db.session.add(organization)
            db.session.commit()
            
            return organization_schema.jsonify(organization), 201

        else:

            return 'Please, pass a valid organization name.', 400

    except Exception as e:

        logging.error("Create Organization: " +  str(e.__class__) + " :" + str(e))
        return "Sorry, couldn't create the organization.", 500

@app.route("/organization/<int:organization_id>/", methods=['PUT'])
def update_organization(organization_id):

    try:

        name = request.json.get('name', '')

        if len(name) > 0:
        
            organization = Organization.query.get(organization_id)
            
            if organization:
                
                organization.name = name
                
                db.session.add(organization)
                db.session.commit()
                
                return organization_schema.jsonify(organization)

            else:

                return 'Please, pass a valid organization id.', 400

        else:

            return 'Please, pass a valid organization name.', 400
    
    except Exception as e:

        logging.error("Update Organization: " +  str(e.__class__) + " :" + str(e))
        return "Sorry, couldn't update the organization.", 500

@app.route("/organization/<int:organization_id>/", methods=['DELETE'])
def delete_organization(organization_id):
    
    try:

        organization = Organization.query.get(organization_id)
        
        if organization:

            db.session.delete(organization)
            db.session.commit()
            
            return organization_schema.jsonify(organization)

        else:

            return 'Please, pass a valid organization id.', 400
    
    except Exception as e:

        logging.error("Delete Organization: " +  str(e.__class__) + " :" + str(e))
        return "Sorry, couldn't delete the organization.", 500

