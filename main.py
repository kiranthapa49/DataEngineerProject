from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker
from typing import List
from csv_loader import load_raw_person
from data_transformer import transform_data
from search import search_persons_by
from format import print_persons
from model import *
from model.raw_person import RawPerson
from model.clean_person import CleanPerson


def clean_tables_if_exists(session):
    session.query(RawPerson).delete()
    session.query(CleanPerson).delete()
    session.commit()


def run_example(session):
    load_raw_person('Raw_Data.csv', session)
    transform_data(session)

    print("Persons with ethnicity as Asian:")
    print_persons(search_persons_by(session, CleanPerson.ethnicity=="Asian"))

    print("Persons with education as High School:")
    print_persons(search_persons_by(session, CleanPerson.education=="High School"))

if __name__ == "__main__" :
        
    conn_str = "sqlite:///persons.db"
    db = create_engine(conn_str)

    Base.metadata.create_all(db)

    Session = sessionmaker(bind=db)
    session = Session()

    clean_tables_if_exists(session)
    run_example(session)
