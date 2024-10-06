import logging
import unittest
from unittest.mock import patch

def log_event(username: str, status: str):
    """
    Logs a login event.

    username: The username logging in.

    status: The status of the login event:
    * success - successful, logged at info level
    * expired - password is expired and should be changed, logged at warning level
    * failed  - password is incorrect, logged at error level
    """
    log_message = f"Login event - Username: {username}, Status: {status}"

    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(message)s'
    )
    logger = logging.getLogger("log_event")

    if status == "success":
        logger.info(log_message)
    elif status == "expired":
        logger.warning(log_message)
    else:
        logger.error(log_message)


class TestLogEvent(unittest.TestCase):

    @patch('logging.getLogger')
    def test_log_success(self, mock_get_logger):
        """Test logging a successful login event."""
        mock_logger = mock_get_logger.return_value

        log_event('testuser', 'success')

        mock_logger.info.assert_called_once_with('Login event - Username: testuser, Status: success')

    @patch('logging.getLogger')
    def test_log_expired(self, mock_get_logger):
        """Test logging an expired password event."""
        mock_logger = mock_get_logger.return_value

        log_event('testuser', 'expired')

        mock_logger.warning.assert_called_once_with('Login event - Username: testuser, Status: expired')

    @patch('logging.getLogger')
    def test_log_failed(self, mock_get_logger):
        """Test logging a failed login event."""
        mock_logger = mock_get_logger.return_value

        log_event('testuser', 'failed')

        mock_logger.error.assert_called_once_with('Login event - Username: testuser, Status: failed')


if __name__ == '__main__':
    unittest.main()
