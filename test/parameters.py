temporary_database = ""

json_r2d2 = {
    	"id":"3",
        "name": "R2-D2",
        "height": "96",
        "mass": "32",
        "hair_color": "n/a",
        "skin_color": "white, blue",
        "eye_color": "red",
        "birth_year": "33BBY",
        "gender": "n/a",
        "homeworld": "8",
        "films": [
            "2",
            "5",
            "4",
            "6",
            "3",
            "1",
            "7"
        ],
        "species": [
            "2"
        ],
        "vehicles": [],
        "starships": []
    }
json_padme ={
        "id": "35",
        "name": "Padmé Amidala",
        "height": "165",
        "mass": "45",
        "hair_color": "brown",
        "skin_color": "light",
        "eye_color": "brown",
        "birth_year": "46BBY",
        "gender": "female",
        "homeworld": "8",
        "films": [
            "5",
            "4",
            "6"
        ],
        "species": [
            "1"
        ],
        "vehicles": [],
        "starships": [
            "9",
            "64",
            "39"
        ],
    }

bad_json_r2d2 = {
        "id":"3",
        "name": "R2-D2",
        "height": "96",
        "mass": "32",
        "hair_color": "n/a",
        "skin_color": "white, blue",
        "eye_color": "red",
        "films": [
            "2",
            "5",
            "4",
            "6",
            "3",
            "1",
            "7"
        ],
        "species": [
            "2"
        ],
        "vehicles": [],
        "starships": []
    }

json_unknow = {
        "id": "00",
        "name": "???",
        "height": "???",
        "mass": "???",
        "hair_color": "???",
        "skin_color": "???",
        "eye_color": "???",
        "birth_year": "???",
        "gender": "???",
        "homeworld": "???",
        "films": [],
        "species": [],
        "vehicles": [],
        "starships": []
    }

create_table_people = '''
    CREATE TABLE people (
    name       TEXT,
    height     TEXT,
    mass       TEXT,
    hair_color TEXT,
    skin_color TEXT,
    eye_color  TEXT,
    birth_year TEXT,
    gender     TEXT,
    homeworld  TEXT,
    films      TEXT,
    species    TEXT,
    vehicles   TEXT,
    starships  TEXT,
    created    TEXT,
    edited     TEXT,
    url        TEXT,
    id         TEXT
    )'''

create_table_films_people = '''CREATE TABLE films_people (
        people TEXT,
        films  TEXT
    );'''

create_table_people_species = '''CREATE TABLE people_species (
        people  TEXT,
        species TEXT
    );'''

create_table_people_starships = '''CREATE TABLE people_starships (
        people    TEXT,
        starships TEXT
    );'''

create_table_people_vehicles = '''CREATE TABLE people_vehicles (
        people   TEXT,
        vehicles TEXT
    );'''

api_url = "http://localhost:8888/people/"