import uuid
from .trips_repository import TripsRepository
from src.models.settings.db_connection_handler import db_connection_handler
from datetime import datetime, timedelta

db_connection_handler.connection()

def test_create_trip():
    conn = db_connection_handler.get_connection()
    trips_repository = TripsRepository(conn)

    trips_infos = {
        "id": str(uuid.uuid4()),
        "destination": "Osasco",
        "start_date": datetime.strptime("02-01-2024", "%d-%m-%Y"),
        "end_date": datetime.strptime("02-01-2024", "%d-%m-%Y") + timedelta(days=5),
        "owner_name": "Osvaldo",
        "owner_email": "osvaldo@email.com"
    }

    trips_repository.create_trip(trips_infos)

    56:52