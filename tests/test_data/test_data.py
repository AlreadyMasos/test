FIRST_TEST_DATA = [('1', '200'), ('2', '200'), ('3', '404'), ('4', '200'),
                   ('5', '200'), ('6', '404'), ('7', '201'), ('8', '200'),
                   ('9', '200'), ('10', '204'), ('11', '200'), ('12', '400'),
                   ('13', '200'), ('14', '400'), ('15', '400')]

GET_DATA = [('1', 'api/users?page=2'), ('2', 'api/users/2'), ('3', 'api/users/23'),
            ('4', 'api/unknown'), ('5', 'api/unknown/2'), ('6', 'api/unknown/23')]

POST_DATA = [({"name": "morpheus", "job": "leader"}, 'api/users', 201, {
    "name": "morpheus", "job": "leader", "id": "93", "createdAt": "2023-03-01T13:30:33.891Z"}),
             ({"email": "eve.holt@reqres.in", "password": "pistol"}, 'api/users/2', 201,
              {"id": 4, "token": "QpwL5tke4Pnpja7X4"}),
             ({"email": "sydney@fife"}, 'api/register', 400, {"error": "Missing password"}),
             ({"email": "eve.holt@reqres.in", "password": "cityslicka"}, 'api/login', 200,
              {"token": "QpwL5tke4Pnpja7X4"}),
             ({"email": "peter@klaven"}, 'api/login', 400, {"error": "Missing password"})]
