import tornado.web as t_web
import database
import json
import jsonschema
import settings
import models.people as people
import dictionary
import schemas
import error


def validate_json_schema(tested_json, expected_json_schema):

    try:
        jsonschema.validate(tested_json, expected_json_schema)

    except Exception as bad_json_schema_exception:

        raise error.ClientError(400,str(bad_json_schema_exception))


class PageHandler(t_web.RequestHandler):

    def json_response(self, data, status=200):
        self.set_status(status)
        self.set_header("Content-Type", 'application/json')
        self.write(data)

    def json_error(self, data, status):
        self.json_response(data, status)


class SWAPIPeopleHandler(PageHandler):

    def prepare(self):
        try:
            self.database = database.Database(settings.SWAPI_DATABASE)

        except error.ServerError as server_error:
            self.finish(server_error.to_json())

    def on_finish(self):
        try:
            self.database.end_connection()

        except error.ServerError as server_error:
            self.json_error(server_error.to_json(),server_error.status)

        except AttributeError :
            pass

    def fetch_people_extra_informations_by_id(self,people):

        [people.add_starship(starship[dictionary.starships])
         for starship in self.database.get_people_starships_by_people_id(people.get_id())]
        [people.add_species(species[dictionary.species])
         for species in self.database.get_people_species_by_people_id(people.get_id())]
        [people.add_film(film[dictionary.films])
         for film in self.database.get_people_films_by_people_id(people.get_id())]
        [people.add_vehicle(vehicle[dictionary.vehicles])
         for vehicle in self.database.get_people_vehicles_by_people_id(people.get_id())]

        return people

    def get(self, people_id):

        try:

            if(people_id):

                people_get = self.database.get_people_by_id(people_id)

                if(people_get):
                    self.json_response(self.fetch_people_extra_informations_by_id(
                        people.People(people_get)).to_json())
                else:
                    raise error.ClientError(404,dictionary.people_not_exists.format(people_id))
            else:

                peoples = self.database.get_peoples()

                peoples_result = []

                [peoples_result.append(self.fetch_people_extra_informations_by_id(people.People(self.database.get_people_by_id(
                    people_get[dictionary.people_id]))).to_json()) for people_get in peoples]
                if(len(peoples_result) == 0):
                    raise error.ClientError(404,dictionary.no_people_in_database)
                else :
                    self.json_response(json.dumps(peoples_result))

        except error.ServerError as server_error:
            self.json_error(server_error.to_json(),server_error.status)

        except error.ClientError as client_error:
            self.json_error(client_error.to_json(),client_error.status)

    def delete(self, people_id):

        try :

            people = self.database.get_people_by_id(people_id)

            if (people):
                self.database.delete_people_by_id(people_id)
                self.json_response(
                    {dictionary.message: dictionary.people_deleted.format(people_id)})
            else:
                raise error.ClientError(404,dictionary.people_not_exists.format(people_id))

        except error.ServerError as server_error:
            self.json_error(server_error.to_json(),server_error.status)

        except error.ClientError as client_error:
            self.json_error(client_error.to_json(),client_error.status)

    def post(self, people_id):

        try:

            json_request_body = json.loads(self.request.body)

            validate_json_schema(json_request_body, schemas.people_json_schema)

            post_people = people.People(json_request_body)

            if(not(self.database.get_people_by_id(post_people.get_id()))):

                self.database.add_people(post_people)
                self.json_response(
                    {dictionary.message: dictionary.people_added.format(post_people.get_id())})
            else:
                raise error.ClientError(403,dictionary.people_already_exists.format(post_people.get_id()))

        except error.ServerError as server_error:
            self.json_error(server_error.to_json(),server_error.status)

        except error.ClientError as client_error:
            self.json_error(client_error.to_json(),client_error.status)

    def put(self, people_id):

        try:

            json_request_body = json.loads(self.request.body)

            validate_json_schema(json_request_body, schemas.people_json_schema)

            put_people = people.People(json_request_body)

            if(self.database.get_people_by_id(put_people.get_id())):

                self.database.update_people(put_people)
                self.json_response(
                    {dictionary.message: dictionary.people_updated.format(put_people.get_id())})
            else:
                raise error.ClientError(404,dictionary.people_not_exists.format(put_people.get_id()))

        except error.ServerError as server_error:
            self.json_error(server_error.to_json(),server_error.status)

        except error.ClientError as client_error:
            self.json_error(client_error.to_json(),client_error.status)
