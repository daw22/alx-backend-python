#!/usr/bin/env python3
"""
Parametrized unit test
"""
from utils import access_nested_map, get_json
import unittest
import requests
from parameterized import parameterized
from unittest.mock import patch


class TestAccessNestedMap(unittest.TestCase):
    """
    Tests utils.access_nested_map function
    """
    @parameterized.expand([
        ({"a": 1}, ("a", ), 1),
        ({"a": {"b": 2}}, ("a", ), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
        ])
    def test_access_nested_map(self, nested_map, path, expected):
        """tests access_nested_map function"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), "KeyError"),
        ({"a": 1}, ("a", "b"), "keyError")
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        """test with invalid key"""
        with self.assertRaises(KeyError):
            self.assertEqual(access_nested_map(nested_map, path), expected)


class TestGetJson(unittest.TestCase):
    """
    Tests utils.get_json function
    """
    @parameterized.expand([
        ("http://example.com", {"Payload": True}),
        ("http://holberton.io", {"Payload": False})
        ])
    @patch("requests.get", )
    def test_get_json(self, test_url, test_payload, mock_get):
        """
        tests utils.get_json by mocking it
        """
        mock_get.return_value.json.return_value = test_payload
        result = get_json(test_url)
        self.assertEqual(result, test_payload)
        mock_get.assert_called_once_with(test_url)


if __name__ == "__main__":
    unittest.main()
