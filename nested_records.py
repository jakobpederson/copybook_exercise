from djcopybook.fixedwidth import Record, fields


class Coverage(Record):
    name = fields.StringField(length=10)


class Ability(Record):
    name = fields.StringField(length=5)
    position = fields.IntegerField(length=1)
    coverages = fields.ListField(Coverage, length=2)


class Job(Record):
    name = fields.StringField(length=5)
    abilities = fields.ListField(Ability, length=3)
    position = fields.IntegerField(length=3)


class Character(Record):
    name = fields.StringField(length=30)
    jobs = fields.ListField(Job, length=3)


data = {
    "Character": {
        "name": "Elrick Whitebone",
        "jobs": [
            {
                "name": "mage",
                "abilities": [
                    {
                        "name": "sneak",
                        "coverages": [
                            {
                                "name": "Mordor"
                            },
                            {
                                "name": "Ereb"
                            }
                        ]
                    }
                ]
            },
            {
                "name": "thief",
                "abilities": [
                    {
                        "name": "fire",
                        "coverages": [
                            {
                                "name": "Arnor"
                            },
                            {
                                "name": "Shire"
                            }
                        ]
                    }
                ]
            },
            {
                "name": "warr",
                "abilities": [
                    {
                        "name": "sword",
                        "coverages": [
                            {
                                "name": "Dale"
                            },
                            {
                                "name": "Mirk"
                            }
                        ]
                    }
                ]
            }
        ]
    }
}


def fields_coverages(ability, data):
    list_data = []
    for coverage in data:
        cov = Coverage()
        cov.name = coverage["name"]
        list_data.append(cov)
    return list_data


def fields_abilities(record, data):
    list_data = []
    for position, ability in enumerate(data, 1):
        new_ability = Ability()
        new_ability.name = ability["name"]
        new_ability.position = position
        new_ability.coverages = fields_coverages(new_ability, ability["coverages"])
        list_data.append(new_ability)
    return list_data


RECORD = {
    "jobs": Job,
    "abilities": Ability,
    "coverages": Coverage,
}



char = Character()
char.name = data["Character"]["name"]
list_data = []
for position, job in enumerate(data["Character"]["jobs"], 1):
    print(job.keys())
    new_job = Job()
    new_job.name = job["name"]
    new_job.position = position
    new_job.abilities = fields_abilities(new_job, job["abilities"])
    list_data.append(new_job)
char.jobs = list_data

print(char.to_record())
