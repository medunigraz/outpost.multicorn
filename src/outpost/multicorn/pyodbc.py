import re
from typing import (
    List,
    Optional,
)

from sqlalchemy.connectors.pyodbc import PyODBCConnector
from sqlalchemy.dialects.oracle.base import OracleDialect
from sqlalchemy.exc import DBAPIError


class OracleDialect_pyodbc(PyODBCConnector, OracleDialect):

    def _get_server_version_info(self, connection) -> Optional[List[int]]:
        try:
            raw = connection.scalar('SELECT * FROM v$version;')
        except DBAPIError:
            return super()._get_server_version_info(connection)
        else:
            r = re.compile(r' (?P<version>[\d\.]+) ')
            matches = r.search(raw)
            if matches:
                version = matches.groupdict().get('version', '0')
                return list(map(int, version.split('.')))
            return None
