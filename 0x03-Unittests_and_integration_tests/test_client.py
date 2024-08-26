#!/usr/bin/env python3
"""
Test module for client.GithubOrgClient
"""
from client import GithubOrgClient
import unittest
from unittest.mock import patch
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


if __name__ == "__main__":
    unittest.main()
