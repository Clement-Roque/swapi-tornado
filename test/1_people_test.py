import parameters
import sys
sys.path.append('./project')

import handlers
import models.people as people
import schemas
import dictionary


def test_people():

    assert handlers.validate_json_schema(parameters.json_r2d2, schemas.people_json_schema) is None
    assert handlers.validate_json_schema(parameters.json_padme, schemas.people_json_schema) is None

    people_for_test = people.People(parameters.json_r2d2)

    assert people_for_test.get_name() == parameters.json_r2d2[dictionary.name]
    assert people_for_test.get_height() == parameters.json_r2d2[dictionary.height]
    assert people_for_test.get_mass() == parameters.json_r2d2[dictionary.mass]
    assert people_for_test.get_hair_color() == parameters.json_r2d2[dictionary.hair_color]
    assert people_for_test.get_skin_color() == parameters.json_r2d2[dictionary.skin_color]
    assert people_for_test.get_eye_color() == parameters.json_r2d2[dictionary.eye_color]
    assert people_for_test.get_birth_year() == parameters.json_r2d2[dictionary.birth_year]
    assert people_for_test.get_gender() == parameters.json_r2d2[dictionary.gender]
    assert people_for_test.get_homeworld() == parameters.json_r2d2[dictionary.homeworld]
    assert people_for_test.get_id() == parameters.json_r2d2[dictionary.people_id]

    assert people_for_test.get_films() == parameters.json_r2d2[dictionary.films]
    assert people_for_test.get_starships() == parameters.json_r2d2[dictionary.starships]
    assert people_for_test.get_species() == parameters.json_r2d2[dictionary.species]
    assert people_for_test.get_vehicles() == parameters.json_r2d2[dictionary.vehicles]

    people_for_test.add_film("8")
    people_for_test.add_species("4")
    people_for_test.add_starship("5")
    people_for_test.add_vehicle("6")

    parameters.json_r2d2[dictionary.films].append("8")
    parameters.json_r2d2[dictionary.starships].append("5")
    parameters.json_r2d2[dictionary.species].append("4")
    parameters.json_r2d2[dictionary.vehicles].append("6")

    assert people_for_test.get_starships() == parameters.json_r2d2[dictionary.starships]
    assert people_for_test.get_films() == parameters.json_r2d2[dictionary.films]
    assert people_for_test.get_species() == parameters.json_r2d2[dictionary.species]
    assert people_for_test.get_vehicles() == parameters.json_r2d2[dictionary.vehicles]

    assert handlers.validate_json_schema(people_for_test.to_json(), schemas.people_json_schema) is None




