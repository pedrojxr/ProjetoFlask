import psycopg2
from psycopg2 import OperationalError 

# path / url de conexão
DB_PATH = "postgresql://neondb_owner:npg_E7ukqhyRcFd8@ep-dawn-snow-ahxmp8lc-pooler.c-3.us-east-1.aws.neon.tech/neondb?sslmode=require"
def get_connection():
        return psycopg2.connect(DB_PATH)
