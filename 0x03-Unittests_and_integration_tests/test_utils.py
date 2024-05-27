#!/usr/bin/env python3
"""
test_utils module
"""
import unittest
from utils import access_nested_map, get_json, memoize
from parameterized import parameterized
from unittest.mock import Mock, patch
import requests


class TestAccessNestedMap(unittest.TestCase):
    """TestAccessNestedMap class"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Test access_nested_map"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """
        Keyerror test
        """
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """
    TestGetJson class test
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch('utils.requests.get')
    def test_get_json(self, test_url, test_payload, mocked_get):
        """
        API mock test
        """
        # define the mocked response
        response = Mock()
        response.json.return_value = test_payload
        mocked_get.return_value = response

        result = get_json(test_url)
        mocked_get.assert_called_once_with(test_url)

        self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):
    """
    TestMemoize class
    """
    def test_memoize(self):
        """
        test memoize
        """
        class TestClass:

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        test_memoize = TestClass()

        with patch.object(test_memoize, 'a_method',
                          return_value=42) as mocked_method:
            result1 = test_memoize.a_property
            result2 = test_memoize.a_property

            mocked_method.assert_called_once()
            self.assertEqual(result1, 42)
            self.assertEqual(result1, 42)


if __name__ == "__main__":
    unittest.main()
