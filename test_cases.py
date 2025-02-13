#!/usr/bin/env python3

from data_extractor import DataExtractor


# Sample text to extract from
text = """
        Contact us at john@email.com or visit https://www.example.com
        Phone: +1234567890 or email: mary@company.com
        """

# Create a data extractor instance
extractor = DataExtractor(text)

"""
Extract, loop through the list of extracted required data
and print them out
"""
emails = extractor.extract_emails()
title = "\nExtracted Emails:"

print(f"\n{title}\n{'-' * len(title)}")
for email in emails:
    print(email)
