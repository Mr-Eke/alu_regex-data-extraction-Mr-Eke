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
    def __init__(self, sample_text: str) -> None:
        """ Initialize objects with the string to be processed """
        self.sample_text: str = sample_text

    def extract_emails(self) -> list[str]:
        """ Extracts and returns a list of emails """
        pattern = r'\b[A-Za-z0-9_%+-]+(?:\.[A-Za-z0-9_%+-]+)*@[A-Za-z0-9-]+(?:\.[A-Za-z0-9-]+)*\.[A-Za-z]{2,}\b'
        return re.findall(pattern, self.sample_text)

    def extract_urls(self) -> list[str]:
        """ Extracts and returns a list of all URLs """
        pattern = r'https?://(?:(?:[-\w]+\.)+[a-zA-Z]{2,}|localhost|\d{1,3}(?:\.\d{1,3}){3})(?::\d{1,5})?(?:/[-\w%.~+]*)*(?:\?[-\w%.~+=&]*)?(?:#[-\w%]*)?'
        return re.findall(pattern, self.sample_text)

    def extract_phone_numbers(self) -> list[str]:
        """ Extract and returns a list of phone numbers """
        pattern = r'\+?\d{1,3}[-.\s]?\d{3,4}[-.\s]?\d{3}[-.\s]?\d{3,4}'
        return re.findall(pattern, self.sample_text)

    def extract_credit_cards(self) -> list[str]:
        """Extracts and returns a list of credit card numbers."""
        pattern = r'\b(?:\d{4}[-\s]?){3}\d{4}\b'
        return re.findall(pattern, self.sample_text)

    def extract_time(self) -> list[str]:
        """Extracts and returns a list of time formats."""
        pattern = r'\b((?:[01]?\d|2[0-3]):[0-5]\d(?:\s?[APap][Mm])?|\b(?:0?[1-9]|1[0-2]):[0-5]\d\s?[APap][Mm])\b'
        return re.findall(pattern, self.sample_text)

    def get_html_tags(self) -> list:
        """ Returns a list of all matching HTML tags."""
        pattern = r'<[^>]+>'
        return re.findall(pattern, self.sample_text)

    def get_hashtags(self) -> list[str]:
        """ Extract and returns a list of all matching hashtags."""
        pattern = r'#[A-Za-z0-9_]+'
        return re.findall(pattern, self.sample_text)

    def get_currency_amounts(self) -> list:
        """ Returns a list of all matching currency amounts."""
        pattern = r'\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?'
        return re.findall(pattern, self.sample_text)
