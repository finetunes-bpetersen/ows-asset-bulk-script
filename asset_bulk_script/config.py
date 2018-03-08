"""Application configuration."""

import json
import logging
import os

import dotenv
from sqlalchemy.pool import NullPool
from sqlalchemy.pool import StaticPool


# Load environment variables from a .env file
dotenv.load('/home/spring/PycharmProjects/ows-asset-bulk-script/.env')

pt = os.getcwd()

test = os.environ.get('TEST')

# Service information
SERVICE_NAME = 'ows-asset-bulk-script'
SERVICE_VERSION = '0.0.1'

# Production environment
PROD_ENVIRONMENT = 'prod'
DEV_ENVIRONMENT = 'dev'
QA_ENVIRONMENT = 'qa'
TEST_ENVIRONMENT = 'test'
ENVIRONMENT = os.environ.get('Environment', DEV_ENVIRONMENT)

# Errors and loggers
SENTRY = os.environ.get('SENTRY_DSN')
LOGGER_DSN = os.environ.get('LOGGER_DSN')
LOGGER_LEVEL = logging.INFO
LOGGER_NAME = 'ows1'

# Database credentials
DB_CREDENTIALS = {
    'database': os.environ.get('AR_PSQL_DATABASE'),
    'host': os.environ.get('AR_PSQL_HOST'),
    'password': os.environ.get('AR_PSQL_PASSWORD'),
    'port': os.environ.get('AR_PSQL_PORT'),
    'user': os.environ.get('AR_PSQL_USER')
}

DB_URL = (
    'postgres://{user}:{password}@{host}:{port}/{db}'
    .format(
        user=DB_CREDENTIALS.get('user'),
        password=DB_CREDENTIALS.get('password'),
        host=DB_CREDENTIALS.get('host'),
        port=DB_CREDENTIALS.get('port'),
        db=DB_CREDENTIALS.get('database')))

path = os.path.dirname(os.path.dirname(__file__))

def _load_schema(schema_name):
    file_name = 'spec/schema/{name}.json'.format(name=schema_name)
    with open(os.path.join(path, file_name)) as f:
        return json.load(f)

# Generic handlers
HEALTH_CHECK = '/hello/'