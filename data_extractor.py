#!/usr/env/python3
"""
This script holds a DataExtractor class to extract emails, URLs, phone numbers,
credit card numbers, time in 12-hour or 24-hour format, HTML tags, hashtags,
and currency amounts from a given API string response using regular expression.
"""

import re


class DataExtractor:
    """
    class for extracting the required data from a string.
    Attributes:
        sample_text (str): The text/string to be processed.
    """

    def __init__(self, sample_text):
        """ Initialize objects with the string to be processed """
        self.sample_text = sample_text

    def extract_emails(self):
        """ Extracts and returns a list of emails """

        pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        return re.findall(pattern, self.sample_text)

    def extract_urls(self):
        """ Extracts and returns a list of all URLs """

        pattern = r'https?://(?:[-\w]|(?:%[\da-fA-F]{2})|\.(?!\.|$))+(?<!\.)'
        return re.findall(pattern, self.sample_text)

    def extract_phone_numbers(self):
        """ Extract and returns a list of phone numbers """

        pattern = r'\+?1?\d{9,15}'
        return re.findall(pattern, self.sample_text)

    def extract_credit_cards(self):
        """Extracts and returns a list of credit card numbers."""

        pattern = r'\b(?:\d{4}[-\s]?){3}\d{4}\b'
        return re.findall(pattern, self.sample_text)



