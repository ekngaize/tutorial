import os

from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv()


def connect_to_yaaps_db():
    required = {
        "YAAPS_DB_NAME": os.getenv("YAAPS_DB_NAME"),
        "YAAPS_DB_USER": os.getenv("YAAPS_DB_USER"),
        "YAAPS_DB_PASSWORD": os.getenv("YAAPS_DB_PASSWORD"),
        "YAAPS_DB_HOST": os.getenv("YAAPS_DB_HOST"),
        "YAAPS_DB_PORT": os.getenv("YAAPS_DB_PORT"),
    }

    missing = [key for key, val in required.items() if not val]
    if missing:
        raise EnvironmentError(f"Missing required environment variables: {', '.join(missing)}")

    db_url = (
        f"postgresql://{required['YAAPS_DB_USER']}:{required['YAAPS_DB_PASSWORD']}"
        f"@{required['YAAPS_DB_HOST']}:{required['YAAPS_DB_PORT']}/{required['YAAPS_DB_NAME']}"
    )

    try:
        engine = create_engine(db_url)
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
    except SQLAlchemyError as e:
        raise ConnectionError(f"Failed to connect to YAAPS database: {e}") from e

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
