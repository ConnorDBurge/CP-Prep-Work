import csv
from os import read


class Fact:
    facts = []
    fact_id = 0

    def __init__(self, id, fact, new_fact=False):
        self.id = id
        self.fact = fact
        if new_fact:
            Fact.write_to_file(self)

    @classmethod
    def all_facts(cls):
        cls.fact_id = 0
        with open(f"./facts.csv") as file:
            dictReader = csv.DictReader(file)
            for fact in dictReader:
                newFact = cls(**fact)
                cls.fact_id += 1
                cls.facts.append(newFact)
        return cls.facts

    @classmethod
    def write_to_file(cls, object):
        with open(f"./facts.csv", 'a+') as csvfile:
            dict_writer = csv.DictWriter(csvfile, ['id', 'fact'])
            dict_writer.writerow(object.__dict__)
