import os

from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv()


def connect_to_yaaps_db():
    db_name = os.getenv("YAAPS_DB_NAME")
    user = os.getenv("YAAPS_DB_USER")
    password = os.getenv("YAAPS_DB_PASSWORD")
    host = os.getenv("YAAPS_DB_HOST")
    port = os.getenv("YAAPS_DB_PORT")
    db_url=f"postgresql://{user}:{password}@{host}:{port}/{db_name}"
    engine = create_engine(db_url)

    return engine


def query_insar_from_pid(pid_list):
    pid_list = ", ".join(f"'{i}'" for i in pid_list)
    query = f"""
            SELECT
                probe_id as pid,
                timestamp,
                value
            FROM egms.mesure_l3
            WHERE mesure_l3.probe_id IN ({pid_list})

            """

    return query
