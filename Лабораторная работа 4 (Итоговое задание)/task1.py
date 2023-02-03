if __name__ == "__main__":
    class Animal:
        def __init__(self, name: str, species: str):
            """
            The base class for all animals
            Initialize the animal's name and species
            :param name: The name of the animal
            :param species: The species of the animal
            """
            self.name = name
            self.species = species

        def __str__(self):
            """Return a string representation of the animal."""
            return f"{self.name} is a {self.species}"

        def __repr__(self):
            """Return a string representation of the animal."""
            return f"Animal('{self.name}', '{self.species}')"


    class Lion(Animal):
        def __init__(self, name: str, species: str = "Lion", area: str = "Africa"):
            """
            A subclass for lions
            Initialize the lion's name, species, and area.
            :param name: The name of the lion
            :param species: The species of the lion
            :param area: The kingdom of the lion
            """
            super().__init__(name, species)
            self._area = area  # private attribute

        def __str__(self):
            """Return a string representation of the lion."""
            return f"{self.name} is a {self.species} from {self._area}"

        def __repr__(self):
            """Return a string representation of the lion."""
            return f"Lion('{self.name}', '{self.species}', '{self._area}')"

        def roar(self) -> str:
            """Return a roar sound made by the lion."""
            return "Roar!"

        def show_kingdom(self) -> str:
            """Return the area of the lion."""
            return self._area
    pass
