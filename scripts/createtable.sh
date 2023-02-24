# bin/bash
/usr/bin/psql -Upostgres -ddw < $AIRFLOW_HOME/scripts/createtable.sql
