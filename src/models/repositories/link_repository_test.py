import pytest
import uuid
from src.models.settings.db_connection_handler import db_connection_handler
from src.models.repositories.link_repository import LinkRepository

db_connection_handler.connect()

link_id = str(uuid.uuid4())
trip_id = str(uuid.uuid4())

@pytest.mark.skip(reason="Interacao com o banco")
def test_registry_links():
    conn = db_connection_handler.get_connection()
    link_repository = LinkRepository(conn)

    links_infos = {
        "id": link_id,
        "trip_id": trip_id,
        "link":  "hoteloscasco.com.br",
        "title": "Hospedagem Hotel Oscaco"
    }

    link_repository.registry_links(links_infos)
    
@pytest.mark.skip(reason="Interacao com o banco")
def test_find_link_from_trip():
        conn = db_connection_handler.get_connection()
        link_repository = LinkRepository(conn)

        link = link_repository.find_links_from_trip(trip_id)
        print()
        print(link)
    
