#!/usr/bin/env python

import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

user = "postgres"
password = "postgres"
database = "flatiron_test"

conn = psycopg2.connect(f"user='{user}' password='{password}'");
conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT);

cur_ob     = conn.cursor()

cur_ob.execute(f"drop database if exists {database};")
cur_ob.execute(f"create database {database};")

print("database created")

