#!/usr/bin/env python3
"""
Test module for client.GithubOrgClient
"""
from client import GithubOrgClient
import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized


class TestGithubOrgClient(unittest.TestCase):
    """
    Contains test cases
    """
    @parameterized.expand([
        ("google"),
        ("abc")
    ])
    @patch("client.get_json")
    def test_org(self, org, mock):
        """
        Tests if GithubOrgClient.org returns the
        correct value
        """
        org_obj = GithubOrgClient(org)
        org_obj.org()
        mock.assert_called_once_with(f'https://api.github.com/orgs/{org}')

    def test_public_repos_url(self):
        """
        Tests the result of _public_repos_url is the expected one
        based on the mocked payload
        """
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mock:
            payload = {"repos_url": "World"}
            mock.return_value = payload
            test_class = GithubOrgClient('test')
            result = test_class._public_repos_url
            self.assertEqual(result, payload["repos_url"])


if __name__ == "__main__":
    unittest.main()
