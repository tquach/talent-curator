import unittest
from talent_curator.apps.google import drive


class GoogleDriveAPITest(unittest.TestCase):

    def setUp(self):
        self.google_api = drive.GoogleDriveAPI()

    def test_build_headers(self):
        headers = self.google_api.build_headers(access_token="hello, world")
        assert headers['Authorization'] == "Bearer hello, world"
