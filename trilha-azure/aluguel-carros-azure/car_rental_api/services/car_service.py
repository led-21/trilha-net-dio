import pandas as pd
from ..models.car import Car

def list_available_cars(conn):
    query = "SELECT * FROM Cars WHERE available = 1"
    cars_df = pd.read_sql(query, conn)
    return cars_df

def add_car(conn, car: Car):
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO Cars (model, brand, year, price_per_day, available) VALUES (?, ?, ?, ?, ?)",
        (car.model, car.brand, car.year, car.price_per_day, True)
    )
    conn.commit()
