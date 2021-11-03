from typing import List
from model.clean_person import CleanPerson

def search_persons_by(session, filter_expr) -> List[CleanPerson]:
    return session.query(CleanPerson).filter(filter_expr).all()
