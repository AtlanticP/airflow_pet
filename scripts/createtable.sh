# bin/bash
/usr/bin/psql -Upostgres -ddw -vpass="'$DB_USER_PASSWORD'" < $AIRFLOW_HOME/scripts/createtable.sql
