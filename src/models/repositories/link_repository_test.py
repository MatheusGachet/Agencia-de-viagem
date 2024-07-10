import pytest
import uuid
from src.models.settings.db_connection_handler import db_connection_handler
from .link_repository import LinkRepository

db_connection_handler.connect()

link_id = str(uuid.uuid4())
trip_id = str(uuid.uuid4())

@pytest.mark.skip(reason="Interacao com o banco")
def test_registry_link():
    conn = db_connection_handler.get_connection()
    link_repository = LinkRepository(conn)

    link_trips_infos = {
        "id": link_id,
        "trip_id": trip_id,
        "link":  "hotel.com.br",
        "title": "Hotel"
    }

    link_repository.registry_link(link_trips_infos)

@pytest.mark.skip(reason="Interacao com o banco")
def test_find_links_from_trip():
        conn = db_connection_handler.get_connection()
        link_repository = LinkRepository(conn)

        links = link_repository.find_links_from_trip(trip_id)
        print()
        print(links)
    
