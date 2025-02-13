#!/usr/bin/env python3

from data_extractor import DataExtractor

# Sample text/string to extract relevant data from
test_string = """
Contact me at c.eke@alustudent.com and for any support
inquiries, reach out to support@alueducation.com. or wdebela@alueducation.com
Visit our website at https://example.com or check our blog at
http://elgibbor.hashnode.dev. You can also reach me at +1234567890
or (987) 654-3210 for business only.
Follow me on social media: https://www.linkedin.com/in/chiago/,
My customer service emails: help@eke.com, info@eke.io, support@eke-chi.co.uk.
Need a job? Send your CV to careers@eke.ai or hr@ekegrp.com.
Scam alert! Ignore fake emails like winner@lottery.com and banking@fraud.net.
Emergency contacts: +1-800-555-0199, +44 7700 900123, or 555-012-3456.
Check this: ftp://files.example.com (Note: an HTTP URL - not extracted).
Email me at first.last123@sub.example.co.in or admin@domain.travel for updates.
need to buy chapati? here are my credit cards are 1234-5678-9876-5432 and
4321 8765 5678 1234. but fear Jesus and dont take morethan $5,000
Don't match this: just a random text. Another one: http://localhost:8000/test
"""

# Create a data extractor instance
extractor = DataExtractor(test_string)

"""
Extract, then loop through the list of extracted
required data and print them out
"""
emails = extractor.extract_emails()
title = "Extracted Emails:"

print(f"\n{title}\n{'-' * len(title)}")  # print a line
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


