
from db.psql_client import PostgresqlClient

class MonitorQuery:
    psql = PostgresqlClient()
    psql = psql.connect()
    