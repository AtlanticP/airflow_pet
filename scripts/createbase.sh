# bin/bash
/usr/bin/psql -Upostgres -dpostgres < $AIRFLOW_HOME/scripts/createbase.sql
