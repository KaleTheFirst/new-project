import sqlite3 

database = './static/data/new-project.db'

 
def insert_flights(flights):
    

    return

def get_all_flights():
    conn = sqlite3.connect(database)
    curs = conn.cursor()
    result = curs.execute("SELECT rowid, * FROM flights")

    flights = []
    for row in result:
        flight = {
            'date': row[0],
            'departure_airport': row[1],
            'departure_scheduled': row[2],
            'arrival_airport': row[3],
            'arrival_scheduled': row[4],
            'airline': row[5],
            'aircraft': row[6]
        }
        flights.append(flight)
    conn.close()
    return flights


          
