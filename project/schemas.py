people_json_schema = {
    "type": "object",
    "properties": {
        "id": {"type": "string"},
        "name": {"type": "string"},
        "birth_year": {"type": "string"},
        "eye_color": {"type": "string"},
        "gender": {"type": "string"},
        "hair_color": {"type": "string"},
        "height": {"type": "string"},
        "mass": {"type": "string"},
        "skin_color": {"type": "string"},
        "homeworld": {"type": "string"},
        "films": {"type": "array"},
        "species": {"type": "array"},
        "starships": {"type": "array"},
        "vehicles": {"type": "array"}
    },
    "additionalProperties": False,
    "required": ["id", "name", "birth_year", "eye_color", "gender", "hair_color", "height", "mass", "skin_color", "homeworld", "films", "species", "starships", "vehicles"]
}
