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
title = "Extracted Emails:"

print(f"\n{title}\n{'-' * len(title)}")
for email in emails:
    print(email)

urls = extractor.extract_urls()
title = "Extracted Urls:"

print(f"\n{title}\n{'-' * len(title)}")
for url_item in urls:
    print(url_item)

phone_nums = extractor.extract_phone_numbers()
title = "Extracted Phone numbers:"

print(f"\n{title}\n{'-' * len(title)}")
for phone_num in phone_nums:
    print(phone_num)


