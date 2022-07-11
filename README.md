# Flask Restful API

Flask restful API + PostgreSQL database

## Running a PostgreSQL database

  (1) Pull PostgreSQL docker image.
  
    docker pull postgres
    
  (2) Create a directory to keep PostgreSQL data.
  
    mkdir postgres-data
      
  (3) Run the image as a container.
  
    sudo docker run -d --name postgres_dev -e POSTGRES_PASSWORD=<postgreSQL_password> -v /home/postgres-data/:/var/lib/postgresql/data -p 5432:5432 postgres

## Runing the API

  (1) Create a config.ini file as follows:

      [DATABASE]

        username = postgres
        password = <postgreSQL_password>
        database = postgres
        host = 172.17.0.1
        port = 5432

  Obs: The host parameter corresponds to PostgreSQL container IP address.
     
  (1) Create the API image.
  
    sudo docker build -t flask_api -f Dockerfile .
    
  (2) Run the api image as a container.
  
      docker run -d -p 5001:5001 flask_api
      
## API endpoints

  ### GET /organization/

  Description: Retrieve all organizations in the database.

  Response: A list of organizations.

  ```javascript
  [
    {
        "id": integer,
        "name": string
    }
  ]
  ```

  ### GET /organization/${int:organization_id}/

  Description: Retrieve a specific organization according to the organization id parameter.

  Request: GET /organization/1

  Response: The organization related to the organization id parameter.

  ```javascript
  {
    "id": integer,
    "name": string
  }
  ```

  ### GET /organization/users/${int:organization_id}/

  Description: Retrieve a user list filtered by organization id.

  Request: GET /organization/users/1

  Response: The users related to the organization id parameter.

  ```javascript
  [
    {
        "email": string,
        "first_name": string,
        "last_name": string
    }
  ]
  ```

  ### POST /organization/

  Description: Create a organization.

  Payload:

  ```javascript
  {
      "name": string
  }
  ```

  Response: The organization that was created.

  ```javascript
  {
    "id": integer,
    "name": string
  }
  ```

  ### PUT /organization/${int:organization_id}/

  Description: Update a specific organization according to the organization id parameter.

  Request: PUT /organization/1

  Payload:

  ```javascript
  {
      "name": string
  }
  ```

  Response: The organization that was updated.

  ```javascript
  {
      "id": integer,
      "name": string
  }
  ```

  ### Delete /organization/${int:organization_id}/

  Description: Delete a specific organization according to the organization id parameter.

  Request: DELETE /organization/1

  Response: The organization that was deleted.

  ```javascript
  {
      "id": integer,
      "name": string
  }
  ```

### GET /user/

  Description: Retrieve all users in the database.
  
  Response: A list of users.
  
  ```javascript
  [
    {
        "email": string,
        "first_name": string,
        "last_name": string
    }
  ]
  ```

### GET /user/${string:user_email}/

  Description: Retrieve a specific user according to the user email parameter.
  
  Request: GET user/user1
  
  Response: The user related to the user email.
  
  ```javascript
  {
      "email": string,
      "first_name": string,
      "last_name": string
  }
  ```
  
  ### POST /user/

  Description: Create a user.
  
  Payload:
  
  ```javascript
  {
      "email": string,
      "first_name": string,
      "last_name": string,
      "organization_id": integer
  }
  ```
  
  Response: The user that was created.
  
  ```javascript
  {
      "email": string,
      "first_name": string,
      "last_name": string
  }
  ```
  
  ### PUT /user/${string:user_email}/

  Description: Update a specific user according to the user email parameter.
  
  Request: PUT user/user1
  
  Payload:
  
  ```javascript
  {
      "email": string,
      "first_name": string,
      "last_name": string,
      "organization_id": integer
  }
  ```
  
  Response: The user that was updated.
  
  ```javascript
  {
      "email": string,
      "first_name": string,
      "last_name": string
  }
  ```
  
  ### Delete /user/${string:user_email}/

  Description: Delete a specific user according to the user email parameter.
  
  Request: DELETE user/user1
  
  Response: The user that was deleted.
  
  ```javascript
  {
      "email": string,
      "first_name": string,
      "last_name": string
  }
  ```
## Status Codes

The API returns the following status codes:

  | Status Code | Description |
  | :--- | :--- |
  | 200 | `OK` |
  | 201 | `CREATED` |
  | 400 | `BAD REQUEST` |
  | 404 | `NOT FOUND` |
  | 500 | `INTERNAL SERVER ERROR` |
