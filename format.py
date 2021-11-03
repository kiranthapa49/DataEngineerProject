from typing import List
from model.clean_person import CleanPerson

def pretty_string_person(person: CleanPerson) -> str:
    return f"""{person.first_name} {person.last_name} 
Born: {person.dob}
Ethnicity: {person.ethnicity}
Education Level: {person.education}
Contact this person by email at: {person.email} 
Or by mail at: {person.address}
"""

def print_persons(persons: List[CleanPerson]) -> None:
    count = len(persons)
    for person in persons:
        print(pretty_string_person(person))
    print(f"Search returned {count} record(s)\n")