import parameters
import sys
sys.path.append('./project')

import settings
import database
import models.people as people
import dictionary



def test_database_connection():

	assert database.Database(parameters.temporary_database)

def test_database_end_connection():

	database_for_test = database.Database(parameters.temporary_database)
	assert database_for_test.end_connection() is None

def test_database_queries():

	database_for_test = database.Database(parameters.temporary_database)

	assert database_for_test.connection.execute(parameters.create_table_people)

	assert database_for_test.connection.execute(parameters.create_table_films_people)
	assert database_for_test.connection.execute(parameters.create_table_people_species)
	assert database_for_test.connection.execute(parameters.create_table_people_starships)
	assert database_for_test.connection.execute(parameters.create_table_people_vehicles)

	assert len(database_for_test.get_peoples()) == 0

	r2d2 = people.People(parameters.json_r2d2)
	padme = people.People(parameters.json_padme)

	
	assert database_for_test.add_people(r2d2) is None
	assert database_for_test.add_people(padme) is None
	
	assert len(database_for_test.get_peoples()) == 2
	assert not(database_for_test.get_people_by_id(padme.get_id()) is None)

	assert people.People(database_for_test.get_people_by_id(padme.get_id())).get_id() == padme.get_id()
	assert people.People(database_for_test.get_people_by_id(padme.get_id())).get_height() == padme.get_height()
	assert people.People(database_for_test.get_people_by_id(padme.get_id())).get_mass() == padme.get_mass()
	assert people.People(database_for_test.get_people_by_id(padme.get_id())).get_hair_color() == padme.get_hair_color()
	assert people.People(database_for_test.get_people_by_id(padme.get_id())).get_skin_color() == padme.get_skin_color()
	assert people.People(database_for_test.get_people_by_id(padme.get_id())).get_eye_color() == padme.get_eye_color()
	assert people.People(database_for_test.get_people_by_id(padme.get_id())).get_birth_year() == padme.get_birth_year()
	assert people.People(database_for_test.get_people_by_id(padme.get_id())).get_gender() == padme.get_gender()
	assert people.People(database_for_test.get_people_by_id(padme.get_id())).get_homeworld() == padme.get_homeworld()
	assert people.People(database_for_test.get_people_by_id(padme.get_id())).get_name() == padme.get_name()
	

	assert len(database_for_test.get_people_films_by_people_id(r2d2.get_id())) == len(r2d2.get_films())
	assert len(database_for_test.get_people_starships_by_people_id(r2d2.get_id()))  == len(r2d2.get_starships())
	assert len(database_for_test.get_people_species_by_people_id(r2d2.get_id()))  == len(r2d2.get_species())
	assert len(database_for_test.get_people_vehicles_by_people_id(r2d2.get_id()))  == len(r2d2.get_vehicles())

	r2d2.add_film("8")
	r2d2.add_species("4")
	r2d2.add_starship("5")
	r2d2.add_vehicle("6")

	assert database_for_test.update_people(r2d2) is None

	assert len(database_for_test.get_people_films_by_people_id(r2d2.get_id())) == len(r2d2.get_films())
	assert len(database_for_test.get_people_starships_by_people_id(r2d2.get_id()))  == len(r2d2.get_starships())
	assert len(database_for_test.get_people_species_by_people_id(r2d2.get_id()))  == len(r2d2.get_species())
	assert len(database_for_test.get_people_vehicles_by_people_id(r2d2.get_id()))  == len(r2d2.get_vehicles())

	assert database_for_test.delete_people_by_id(r2d2.get_id()) is None

	assert len(database_for_test.get_people_films_by_people_id(r2d2.get_id())) == 0
	assert len(database_for_test.get_people_starships_by_people_id(r2d2.get_id()))  == 0
	assert len(database_for_test.get_people_species_by_people_id(r2d2.get_id()))  == 0
	assert len(database_for_test.get_people_vehicles_by_people_id(r2d2.get_id()))  == 0

	assert database_for_test.get_people_by_id(r2d2.get_id()) is None
	assert len(database_for_test.get_peoples()) == 1	

	database_for_test.end_connection()