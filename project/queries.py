get_all_peoples = ''' SELECT id,
name,
birth_year,
eye_color,
gender,
hair_color,
height,
mass,
skin_color,
homeworld,
films,
species,
vehicles,
starships
FROM PEOPLE '''

get_people_by_people_id = ''' SELECT id,
name,
birth_year,
eye_color,
gender,
hair_color,
height,
mass,
skin_color,
homeworld,
films,
species,
vehicles,
starships
FROM PEOPLE 
WHERE id = ? '''

delete_people_by_people_id = ''' 
DELETE FROM PEOPLE WHERE id = ?'''

delete_films_people_match_by_people_id = ''' 
DELETE FROM FILMS_PEOPLE WHERE people = ?'''

delete_people_species_match_by_people_id = ''' 
DELETE FROM PEOPLE_SPECIES WHERE people = ?'''

delete_people_starships_match_by_people_id = ''' 
DELETE FROM PEOPLE_STARSHIPS WHERE people = ?'''

delete_people_vehicles_match_by_people_id = ''' 
DELETE FROM PEOPLE_VEHICLES WHERE people = ?'''

get_people_vehicles_by_people_id = ''' SELECT 
vehicles
FROM PEOPLE_VEHICLES
WHERE people = ? '''

get_people_starships_by_people_id = ''' SELECT 
starships
FROM PEOPLE_STARSHIPS
WHERE people = ? '''

get_people_films_by_people_id = ''' SELECT 
films
FROM FILMS_PEOPLE
WHERE people = ? '''

get_people_species_by_people_id = ''' SELECT 
species
FROM PEOPLE_SPECIES
WHERE people = ? '''

add_people = '''
INSERT INTO PEOPLE (
	name,
    height,
    mass,
    hair_color,
    skin_color,
    eye_color,
    birth_year,
    gender,
    homeworld,
    films,
    species,
    vehicles,
    starships,
    created,
    edited,
    url,
    id) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)'''
add_films_people_match_by_ids = ''' 
INSERT INTO FILMS_PEOPLE (films, people) VALUES (?,?)'''

add_people_species_match_by_ids = ''' 
INSERT INTO PEOPLE_SPECIES (people, species) VALUES (?,?)'''

add_people_starship_match_by_ids = ''' 
INSERT INTO PEOPLE_STARSHIPS (people, starships) VALUES (?,?)'''

add_match_people_vehicle_by_ids = ''' 
INSERT INTO PEOPLE_VEHICLES (people, vehicles) VALUES (?,?)'''

update_people = '''
UPDATE PEOPLE SET
	name = ?,
    height = ?,
    mass = ?,
    hair_color = ?,
    skin_color = ?,
    eye_color = ?,
    birth_year = ?,
    gender = ?,
    homeworld = ?,
    edited = ? 
    WHERE id = ?
'''
