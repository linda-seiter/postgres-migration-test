#!/usr/bin/env python

import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

user = "postgres"
password = "postgres"
database = "labs"

conn = psycopg2.connect(f"user='{user}' password='{password}'");
conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT);

cur_ob     = conn.cursor()

cur_ob.execute(f"DROP DATABASE IF EXISTS {database};")
cur_ob.execute(f"CREATE DATABASE {database};")

# print(f"database {database} created")

