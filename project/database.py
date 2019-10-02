import sqlite3
import queries
from datetime import datetime
import error


def dictionary_factory(cursor, row):
    dictionary = {}
    for index, column in enumerate(cursor.description):
        dictionary[column[0]] = row[index]
    return dictionary


class Database:
    def __init__(self,database_to_connect):
        try:
            self.connection = sqlite3.connect(database_to_connect)
            self.connection.row_factory = dictionary_factory

        except sqlite3.Error as database_create_connection_error:
            print(database_create_connection_error)
            raise error.ServerError(500)

    def end_connection(self):
        try:
            self.connection.close()

        except sqlite3.Error as database_close_connection_error:
            print(database_close_connection_error)
            raise error.ServerError(500)

    def get_peoples(self):

        try:
            return self.connection.execute(queries.get_all_peoples).fetchall()

        except sqlite3.Error as execute_query_exception:
            print(execute_query_exception)
            raise error.ServerError(500)

    def get_people_by_id(self, people_id):

        try:
            return self.connection.execute(queries.get_people_by_people_id, (people_id,)).fetchone()

        except sqlite3.Error as execute_query_exception:
            print(execute_query_exception)
            raise error.ServerError(500)

    def delete_people_by_id(self, people_id):

        try:
            self.connection.execute(
                queries.delete_films_people_match_by_people_id, (people_id,))
            self.connection.execute(
                queries.delete_people_species_match_by_people_id, (people_id,))
            self.connection.execute(
                queries.delete_people_starships_match_by_people_id, (people_id,))
            self.connection.execute(
                queries.delete_people_vehicles_match_by_people_id, (people_id,))
            self.connection.execute(
                queries.delete_people_by_people_id, (people_id,))
            self.connection.commit()

        except sqlite3.Error as execute_query_exception:

            print(execute_query_exception)
            raise error.ServerError(500)

    def get_people_vehicles_by_people_id(self, people_id):

        try:
            return self.connection.execute(queries.get_people_vehicles_by_people_id, (people_id,)).fetchall()

        except sqlite3.Error as execute_query_exception:

            print(execute_query_exception)
            raise error.ServerError(500)

    def get_people_starships_by_people_id(self, people_id):

        try:
            return self.connection.execute(queries.get_people_starships_by_people_id, (people_id,)).fetchall()

        except sqlite3.Error as execute_query_exception:

            print(execute_query_exception)
            raise error.ServerError(500)

    def get_people_films_by_people_id(self, people_id):

        try:
            return self.connection.execute(queries.get_people_films_by_people_id, (people_id,)).fetchall()

        except sqlite3.Error as execute_query_exception:

            print(execute_query_exception)
            raise error.ServerError(500)

    def get_people_species_by_people_id(self, people_id):

        try:
            return self.connection.execute(queries.get_people_species_by_people_id, (people_id,)).fetchall()

        except sqlite3.Error as execute_query_exception:

            print(execute_query_exception)
            raise error.ServerError(500)

    def add_people(self, people):

        post_date_time = datetime.now()
        try:

            self.connection.execute(queries.add_people, (
                people.get_name(),
                people.get_height(),
                people.get_mass(),
                people.get_hair_color(),
                people.get_skin_color(),
                people.get_eye_color(),
                people.get_birth_year(),
                people.get_gender(),
                people.get_homeworld(),
                None,
                None,
                None,
                None,
                post_date_time,
                post_date_time,
                people.get_id(),
                people.get_id())
            )

            [self.connection.execute(queries.add_films_people_match_by_ids, (
                films_id, people.get_id())) for films_id in people.get_films()]
            [self.connection.execute(queries.add_people_species_match_by_ids, (people.get_id(
            ), species_id)) for species_id in people.get_species()]
            [self.connection.execute(queries.add_people_starship_match_by_ids, (people.get_id(
            ), starship_id)) for starship_id in people.get_starships()]
            [self.connection.execute(queries.add_match_people_vehicle_by_ids, (people.get_id(
            ), vehicle_id)) for vehicle_id in people.get_vehicles()]

            self.connection.commit()

        except sqlite3.Error as execute_query_exception:

            print(execute_query_exception)
            raise error.ServerError(500)

    def update_people(self, people):

        post_date_time = datetime.now()
        try:

            self.connection.execute(
                queries.delete_films_people_match_by_people_id, (people.get_id(),))
            self.connection.execute(
                queries.delete_people_species_match_by_people_id, (people.get_id(),))
            self.connection.execute(
                queries.delete_people_starships_match_by_people_id, (people.get_id(),))
            self.connection.execute(
                queries.delete_people_vehicles_match_by_people_id, (people.get_id(),))

            self.connection.execute(queries.update_people, (
                people.get_name(),
                people.get_height(),
                people.get_mass(),
                people.get_hair_color(),
                people.get_skin_color(),
                people.get_eye_color(),
                people.get_birth_year(),
                people.get_gender(),
                people.get_homeworld(),
                post_date_time,
                people.get_id())
            )

            [self.connection.execute(queries.add_films_people_match_by_ids, (
                films_id, people.get_id())) for films_id in people.get_films()]
            [self.connection.execute(queries.add_people_species_match_by_ids, (people.get_id(
            ), species_id)) for species_id in people.get_species()]
            [self.connection.execute(queries.add_people_starship_match_by_ids, (people.get_id(
            ), starship_id)) for starship_id in people.get_starships()]
            [self.connection.execute(queries.add_match_people_vehicle_by_ids, (people.get_id(
            ), vehicle_id)) for vehicle_id in people.get_vehicles()]

            self.connection.commit()

        except sqlite3.Error as execute_query_exception:

            print(execute_query_exception)
            raise error.ServerError(500)
