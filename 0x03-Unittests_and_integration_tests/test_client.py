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

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """Test that public_repos returns the correct list of repos"""
        test_payload = [
            {
                "name": "yimbo",
                "id": 2233424,
                "private": False,
                "owner": {
                    "login": "google",
                    "id": 240297
                    },
                "fork": False,
                "url": "https://api.github.com/orgs/google/yimbo",
                "created_at": "2024-03-12T00:00:12Z",
                "updated_at": "2024-04-23T00:43:52Z",
                "has_issues": False,
                "forks": 46,
                "default_branch": "main"
            },
            {
                "name": "genealatics",
                "id": 3433452,
                "private": False,
                "owner": {
                    "login": "google",
                    "id": 240297
                    },
                "fork": False,
                "url": "https://api.github.com/orgs/google/genealatics",
                "created_at": "2024-04-07T00:40:12Z",
                "updated_at": "2024-05-13T00:53:52Z",
                "has_issues": False,
                "forks": 156,
                "default_branch": "main"
            }
        ]
        mock_get_json.return_value = test_payload

        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock_public_repos_url:
            url = "https://api.github.com/orgs/test_org/repos"
            mock_public_repos_url.return_value = url

            client = GithubOrgClient("test_org")
            result = client.public_repos()

            # Check if the result matches the expected list of repo names
            self.assertEqual(result, ["yimbo", "genealatics"])

            # Check if the mocked property and get_json were called once
            mock_public_repos_url.assert_called_once()
            mock_get_json.assert_called_once_with(url)


if __name__ == "__main__":
    unittest.main()
