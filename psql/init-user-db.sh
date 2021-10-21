#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --username postgres <<-EOSQL
    CREATE USER qytanguser;
    CREATE DATABASE qytangdb;
    GRANT ALL PRIVILEGES ON DATABASE qytangdb TO qytanguser;
    ALTER USER qytanguser WITH PASSWORD 'Cisc0123';
EOSQL