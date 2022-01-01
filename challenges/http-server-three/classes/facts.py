import csv
from os import read


class Fact:
    facts = []

    def __init__(self, id, fact):
        self.id = id
        self.fact = fact

    @classmethod
    def all_facts(cls):
        with open(f"./facts.csv") as file:
            dictReader = csv.DictReader(file)
            for fact in dictReader:
                newFact = cls(**fact)
                cls.facts.append(newFact)
        return cls.facts
