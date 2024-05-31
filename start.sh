#!/bin/bash

airflow webserver --port 8000 &

sleep 10

airflow scheduler &

wait