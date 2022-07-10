from api import *

@app.route("/user/")
def list_users():

    try:
  
        users = User.query.all()

        for user in users:

            organization = Organization.query.get(user.organization_id)

            if organization:
                
                user.email = user.email + '@' + organization.name + '.com'

        return jsonify(users_schema.dump(users))

    except Exception as e:

        logging.error("List Users: " +  str(e.__class__) + " :" + str(e))
        return "Sorry, couldn't retrieve the users.", 500

@app.route("/user/<string:user_email>/")
def get_user(user_email):

    try:

        user = User.query.get(user_email)

        organization = Organization.query.get(user.organization_id)

        if organization:
            
            user.email = user.email + '@' + organization.name + '.com'

        return user_schema.jsonify(user)

    except Exception as e:

        logging.error("Get User: " +  str(e.__class__) + " :" + str(e))
        return "Sorry, couldn't retrieve the user.", 500

@app.route("/user/", methods=['POST'])
def create_user():

    try:

        email = request.json.get('email', '')
        first_name = request.json.get('first_name', '')
        last_name = request.json.get('last_name', '')
        organization_id = request.json.get('organization_id', '')

        if len(email) > 0 and len(first_name) > 0 and len(last_name) > 0 and organization_id:
            
            user = User(email, first_name, last_name, organization_id)
            
            db.session.add(user)
            db.session.commit()
            
            return user_schema.jsonify(user), 201

        else:

            return 'Please, pass a valid email, first_name, last_name e organization_id.', 400

    except Exception as e:

        logging.error("Create User: " +  str(e.__class__) + " :" + str(e))
        return "Sorry, couldn't create the user.", 500

@app.route("/user/<string:user_email>/", methods=['PUT'])
def update_user(user_email):

    try:

        email = request.json.get('email', '')
        first_name = request.json.get('first_name', '')
        last_name = request.json.get('last_name', '')
        organization_id = request.json.get('organization_id', '')

        if len(email) > 0 and len(first_name) > 0 and len(last_name) > 0 and organization_id:

            user = User.query.get(user_email)

            if user:

                user.email = email
                user.first_name = first_name
                user.last_name = last_name
                user.organization_id = organization_id 
                
                db.session.add(user)
                db.session.commit()
                
                return user_schema.jsonify(user)

            else:

                return 'Please, pass a valid user email.', 400
        
        else:

            return 'Please, pass a valid email, first_name, last_name e organization_id.', 400

    except Exception as e:

        logging.error("Update User: " +  str(e.__class__) + " :" + str(e))
        return "Sorry, couldn't update the user.", 500

@app.route("/user/<string:user_email>/", methods=['DELETE'])
def delete_user(user_email):
    
    try:

        user = User.query.get(user_email)
        
        if user:

            db.session.delete(user)
            db.session.commit()
            
            return user_schema.jsonify(user)

        else:

            return 'Please, pass a valid user email.', 400

    except Exception as e:

        logging.error("Delete User: " +  str(e.__class__) + " :" + str(e))
        return "Sorry, couldn't delete the user.", 500

