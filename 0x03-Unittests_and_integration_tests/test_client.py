#!/usr/bin/env python3
"""
test_client module
"""
import unittest
from parameterized import parameterized
from unittest.mock import Mock, patch
from client import GithubOrgClient
import requests


class TestGithubOrgClient(unittest.TestCase):
    """TestGithubOrgClient test"""
    @parameterized.expand([
        ("google",),
        ("abc",)
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """
        test_org method
        """
        mock_get_json.return_value = {"login": org_name}

        client = GithubOrgClient(org_name)
        result = client.org

        self.assertEqual(result, {'login': org_name})

        url = "https://api.github.com/orgs"

        mock_get_json.assert_called_once_with(f"{url}/{org_name}")


if __name__ == "__main__":
    unittest.main()
