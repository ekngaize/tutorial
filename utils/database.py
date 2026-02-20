from sqlalchemy import create_engine

def connect_to_yaaps_db(credentials):
    db_name = "insar_to_rga"
    user = credentials['user']
    password = credentials['password']
    host = "192.168.100.39"
    port = "5432"

    engine = create_engine(f"postgresql://{user}:{password}@{host}:{port}/{db_name}")

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