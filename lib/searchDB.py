def searchDB(TEXT, db_credentials):
    import cx_Oracle

    connection = cx_Oracle.connect(str(db_credentials))

    cursor = connection.cursor()

    cursor.execute(
        """
        SQL script
        """,
        text=str(TEXT)
    )

    for fname in cursor: print("Values:", fname)