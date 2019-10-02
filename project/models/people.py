import dictionary


class People:

    def __init__(self, people):
        self.id = people[dictionary.people_id]
        self.name = people[dictionary.name]
        self.birth_year = people[dictionary.birth_year]
        self.eye_color = people[dictionary.eye_color]
        self.gender = people[dictionary.gender]
        self.hair_color = people[dictionary.hair_color]
        self.height = people[dictionary.height]
        self.mass = people[dictionary.mass]
        self.skin_color = people[dictionary.skin_color]
        self.homeworld = people[dictionary.homeworld]
        self.films = []
        self.species = []
        self.starships = []
        self.vehicles = []

        if (people[dictionary.films]):
            self.films = people[dictionary.films]
        if (people[dictionary.species]):
            self.species = people[dictionary.species]
        if (people[dictionary.starships]):
            self.starships = people[dictionary.starships]
        if (people[dictionary.vehicles]):
            self.vehicles = people[dictionary.vehicles]

    def add_film(self, film):
        self.films.append(film)

    def add_species(self, species):
        self.species.append(species)

    def add_starship(self, starship):
        self.starships.append(starship)

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)

    def get_films(self):
        return self.films

    def get_species(self):
        return self.species

    def get_starships(self):
        return self.starships

    def get_vehicles(self):
        return self.vehicles

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_birth_year(self):
        return self.birth_year

    def get_eye_color(self):
        return self.eye_color

    def get_gender(self):
        return self.gender

    def get_hair_color(self):
        return self.hair_color

    def get_height(self):
        return self.height

    def get_mass(self):
        return self.mass

    def get_skin_color(self):
        return self.skin_color

    def get_homeworld(self):
        return self.homeworld

    def to_json(self):
        return {
            dictionary.people_id: self.id,
            dictionary.name: self.name,
            dictionary.birth_year: self.birth_year,
            dictionary.eye_color: self.eye_color,
            dictionary.gender: self.gender,
            dictionary.hair_color: self.hair_color,
            dictionary.height: self.height,
            dictionary.mass: self.mass,
            dictionary.skin_color: self.skin_color,
            dictionary.homeworld: self.homeworld,
            dictionary.films: self.films,
            dictionary.species: self.species,
            dictionary.starships: self.starships,
            dictionary.vehicles: self.vehicles,
        }
