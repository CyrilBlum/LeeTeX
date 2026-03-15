from sqlite3 import *
import pandas as pd

# Verbindung zur DB demo.db öffnen
with connect("school.db") as con:
    # Datenbank-Cursor (=Lese/Schreibestift) holen
    cursor = con.cursor()

    # SQL-Code zur Erstellung der Tabelle
    sql = """
        CREATE TABLE IF NOT EXISTS students (
            first_name VARCHAR(255),
            last_name VARCHAR(255),
            year_of_entry INTEGER,
            date_of_birth DATE
        )
    """

    # SQL ausführen
    cursor.execute("DROP TABLE IF EXISTS students;")
    cursor.execute(sql)

    # insert
    sql = """
        INSERT INTO students (first_name, last_name, year_of_entry, date_of_birth)
        VALUES
           ('{}', '{}', {}, {})
    """.format(
        "Cyril", "Blum", 20 + 2, "1992-11-07"
    )

    cursor.execute(sql)
    cursor.execute("SELECT * FROM students")
    df = pd.read_sql_query("SELECT * FROM students", con)
    print(df.to_markdown())
