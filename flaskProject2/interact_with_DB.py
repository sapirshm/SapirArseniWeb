from flask import jsonify
import mysql.connector
import json


# ------------------------------------------------- #
# ------------- DATABASE CONNECTION --------------- #
# ------------------------------------------------- #
def interact_db(query, query_type: str):
    return_value = False
    # creating a connection to the db
    connection = mysql.connector.connect(host='localhost',
                                         user='root',
                                         passwd='root',
                                         database='assignment10db')
    #  db cursor - this object executes sql queries
    cursor = connection.cursor(named_tuple=True)
    cursor.execute(query)

    if query_type == 'commit':
        # Use for INSERT, UPDATE, DELETE statements.
        # Returns: The number of rows affected by the query (a non-negative int).
        connection.commit()
        return_value = True

    if query_type == 'fetch':
        # Use for SELECT statement.
        # Returns: False if the query failed, or the result of the query if it succeeded.
        query_result = cursor.fetchall()
        return_value = query_result

    connection.close()
    cursor.close()
    return return_value


def query_to_json(query):
    connection = mysql.connector.connect(host='localhost',
                                         user='root',
                                         passwd='root',
                                         database='assignment10db')
    #  db cursor - this object executes sql queries
    cursor = connection.cursor(dictionary=True)
    cursor.execute(query)
    result = cursor.fetchall()

    connection.close()
    cursor.close()
    return result