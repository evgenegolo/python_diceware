from pymysql import *

credentials = {"host": '127.0.0.1', "username": 'root', "password": '', "db": 'PYpass'}


def connect_db():
    """
    Function is responsible to set connection to a database
    :return: Database connection object
    """
    connection = None  # Database connection reference
    try:  # Try to connect and work with the specific database
        if connection is None:
            connection = connect(host=credentials['host'], user=credentials['username'],
                                 database=credentials['db'], password=credentials['password'],
                                 cursorclass=cursors.DictCursor)
    except MySQLError:  # If there was a problem while connecting the database
        print("Couldn't connect the database")

    return connection


def fetch_records(query: str) -> object:
    """
    Function is responsible to count rows, according to the given query
    :param query: SQL query to execute
    :return: Rows that were effected by the query, None if there was a problem fetching results
    """
    connection = connect_db()

    if connection is not None:
        with connection.cursor() as cursor:
            # Query to execute
            cursor.execute(query)
            connection.commit()
            connection.close()

            records = cursor.fetchall()  # Getting all records
            return records
    return None
