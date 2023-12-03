"""
Test custom Django management commands.
"""

from unittest.mock import patch

from psycopg2 import OperationalError as PsycopgError

from django.core.management import call_command
from django.db.utils import OperationalError
from django.test import SimpleTestCase

@patch('core.management.commands.wait_for_db.Command.check')
class CommandTests(SimpleTestCase):
    """Test custom Django management commands."""

    def test_wait_for_db_ready(self, patched_check):
        """Test waiting for db when db is available."""

        patched_check.return_value = True

        call_command('wait_for_db')

        patched_check.assert_called_once_with(database=['default'])
