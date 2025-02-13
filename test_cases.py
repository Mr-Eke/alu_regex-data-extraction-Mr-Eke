#!/usr/bin/env python3

from data_extractor import DataExtractor


# Sample text/string to extract relevant data from
test_string = """
Contact me at john.doe@example.com and support@company.org for inquiries.
Visit our website at https://example.com or check our blog at http://blog.example.net.
You can also reach us at +1234567890 or (987) 654-3210 for support.
Follow us on social media: https://twitter.com/user, http://facebook.com/page,
and https://linkedin.com/in/user-profile.
Our customer service emails: help@service.com, info@business.io,
support@xyz-company.co.uk.
Need a job? Send your CV to careers@startup.ai or hr@bigcorp.com.
Scam alert! Ignore fake emails like winner@lottery.com and banking@fraud.net.
Click on this suspicious link: http://phishing-site.com/login?user=you
Emergency contacts: +1-800-555-0199, +44 7700 900123, or 555-012-3456.
Check this out: ftp://files.example.com (Note: Should not be detected as an HTTP URL).
Email me at first.last123@sub.example.co.in or admin@domain.travel for updates.
Random text with no emails, no URLs, and no phone numbers to test false positives.
"""

# Create a data extractor instance
extractor = DataExtractor(test_string)

"""
Extract, then loop through the list of extracted
required data and print them out
"""
emails = extractor.extract_emails()
title = "Extracted Emails:"

print(f"\n{title}\n{'-' * len(title)}")  # line
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


