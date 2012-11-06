import unittest
import talent_curator
import requests


class TalentCuratorCandidatesTests(unittest.TestCase):

    def setUp(self):
        talent_curator.app.config['TESTING'] = True
        self.app = talent_curator.app.test_client()

    def test_should_route_to_index(self):
        rv = self.app.get('/')
        assert rv.status_code == requests.codes.ok

    def tearDown(self):
        pass
