def stream_rows(connection, batch_size=1):
    """
    Generator that streams rows from the user_data table one by one (or in batches).
    """
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM user_data;")

    while True:
        rows = cursor.fetchmany(batch_size)  # get limited rows from DB
        if not rows:  # if no more rows, stop
            break
        for row in rows:  # yield rows one by one
            yield row

    cursor.close()
