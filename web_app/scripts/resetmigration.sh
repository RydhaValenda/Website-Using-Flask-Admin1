#!/bin/sh
alembic downgrade base
rm -rf migrations/versions/*
alembic revision --autogenerate -m 'Initial db'
alembic upgrade head
