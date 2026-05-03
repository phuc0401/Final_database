import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",       # máy tính của bạn
        user="root",            # user MySQL
        password="1234",        # password MySQL của bạn
        database="sport_tickets"# tên database
    )