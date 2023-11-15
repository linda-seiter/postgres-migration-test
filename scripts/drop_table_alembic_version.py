#!/usr/bin/env python
#
# Small script to show PostgreSQL and Pyscopg together
#

import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

user = "postgres"
password = "postgres"
database = "flatiron_test"

conn = psycopg2.connect(f"dbname={database} user='{user}' host='localhost' password='{password}'")
conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT);

cur_ob     = conn.cursor()

cur_ob.execute(f"DROP TABLE IF EXISTS alembic_version;")

# print("table alembic_version dropped")
