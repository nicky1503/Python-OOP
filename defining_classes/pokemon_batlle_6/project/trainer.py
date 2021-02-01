


class Trainer:
    def __init__(self, name):
        self.name = name
        self.pokemon = []

    def add_pokemon(self, pokemon):
        if pokemon not in self.pokemon:
            self.pokemon.append(pokemon)
            return f"Caught {pokemon.pokemon_details()}"
        else:
            return "This pokemon is already caught"

    def release_pokemon(self, pokemon_name):
        if any(True for x in self.pokemon if x.name == pokemon_name):
            self.pokemon = [x for x in self.pokemon if x.name != pokemon_name]
            return f"You have released {pokemon_name}"
        else:
            return "Pokemon is not caught"

    def trainer_data(self):
        result = "\n".join([p.pokemon_details() for p in self.pokemon])
        return f'Pokemon Trainer {self.name}\nPokemon count {len(self.pokemon)}\n' + result
 








