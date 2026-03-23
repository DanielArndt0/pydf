from __future__ import annotations

"""MySQL helpers used when database persistence is enabled."""

from contextlib import contextmanager
from typing import Iterator

import mysql.connector

from .config import DatabaseConfig
from .models import InvoiceRecord


@contextmanager
def mysql_connection(config: DatabaseConfig) -> Iterator[mysql.connector.MySQLConnection]:
    """Create and automatically close a MySQL connection."""
    connection = mysql.connector.connect(
        host=config.host,
        user=config.user,
        password=config.password,
        database=config.database,
    )
    try:
        yield connection
    finally:
        connection.close()


def insert_record(connection: mysql.connector.MySQLConnection, config: DatabaseConfig, record: InvoiceRecord) -> None:
    """Insert one processed record into the configured MySQL table."""
    sql = (
        f"INSERT INTO {config.table} "
        "(invoice_number, invoice_date, file_name, status) VALUES (%s, %s, %s, %s)"
    )
    values = (record.invoice_number, record.invoice_date, record.file_name, record.status)
    cursor = connection.cursor()
    try:
        cursor.execute(sql, values)
        connection.commit()
    finally:
        cursor.close()
