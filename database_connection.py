from flask import Flask
import psycopg2

def connect_to_database():
    try:
        conn = psycopg2.connect(
            host="team8.postgres.database.azure.com",
            database="postgres",
            user="team8",
            password="server1234!"
        )
        print("Good connection")
    except:
        print("Unable to connect to the database")