#!/usr/bin/env python3
"""
test_client module
"""
import unittest
from parameterized import parameterized
from unittest.mock import Mock, patch, PropertyMock
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

    @parameterized.expand([
        ("google", "https://api.github.com/orgs/google/repos"),
        ("abc", "https://api.github.com/orgs/abc/repos")
    ])
    def test_public_repos_url(self, org_name, expected_url):
        """
        test_public_repos_url
        """
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mock_org:
            mock_org.return_value = {"repos_url": expected_url}

            client = GithubOrgClient(org_name)
            result = client._public_repos_url

            self.assertEqual(result, expected_url)


if __name__ == "__main__":
    unittest.main()
