

def transform_data(session):
    query = """
        INSERT INTO clean(
            first_name,
            last_name,
            address,
            email,
            dob,
            ethnicity,
            education
        )
        SELECT
            first_name,
            last_name,
            address,
            email,
            dob,
            ethnicity,
            education
        FROM raw WHERE ethnicity= :ethnicity OR education=:education
    """

    session.execute(query, dict(ethnicity="Asian", education="High School"))
    session.commit()
