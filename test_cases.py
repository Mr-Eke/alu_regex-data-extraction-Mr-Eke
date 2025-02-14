#!/usr/bin/env python3

from data_extractor import DataExtractor

# Sample text/string to extract relevant data from
test_string = """
======= Edge Cases: Invalid Email Addresses ========

o'connor@example.com "very.unusual.@.unusual.com"@example.com
"user\\\"name"@example.com user@[192.168.1.1]
My email is user(at)example.com user@@example.com user@example..com.
user@, user.example.com  # (Invalid: missing @)
example.emailaddress.com  # (Invalid: looks like a domain, not an email)
"email": "user@example,com"  # (Invalid: comma instead of dot)

============ Valid Email Addresses =============

eke-chi.me@example.co.uk alt email: eke101.c@alustudent.com
Contact me at c.eke@alustudent.com and for any support inquiries,
reach out to support@alueducation.com.
emails in bracket (braces@example.org) <anglebracket@example.org>

 ========= Edge Cases: Invalid URLs (Not Matched) =========

    "http:/example.com",        - Missing slash
    "https//example.com",       - Missing colon
    "ftp:example.com",          - Missing slashes
    "://example.com",           - Missing protocol
    "https://", https://        - Missing domain
    "https://.com",             - Missing domain name
    "https://example",          - Missing TLD
     https://.eke.com",         - Domain starts with dot
    "https://example..com",     - Consecutive dots
    "https://exam ple.com",     - Space in domain
    "https://exam_ple.com",     - Underscore in domain name (invalid)

============== Valid Urls (Matched) ===============

    "https://eke.com/#", https://eke.com. checkout my socials and connect
     with me at https://www.linkedin.com/in/chiago/, http://www.eke-chi.tech

============ Edge Cases: Phone numbers (Different formats) =============

(123) 456-7890 or call the below numbers
123-456-7890 123.456.7890. you can  also reach Herve at
+250788899944, +1 123-456-7890.

==================== credit Card =====================
1234 5678 9012 3456
1234-5678-9012-3456

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
print("\n".join(emails) if emails else "No URLs found")
print('---')

urls = extractor.extract_urls()
title = "Extracted Urls:"

print(f"\n{title}\n{'-' * len(title)}")
print("\n".join(urls) if urls else "No URLs found")
print('---')

phone_nums = extractor.extract_phone_numbers()
title = "Extracted Phone numbers:"

print(f"\n{title}\n{'-' * len(title)}")
print("\n".join(phone_nums) if phone_nums else "No phone number found")
print('---')

card = extractor.extract_credit_cards()
title = "Extracted Credit Card Numbers:"

print(f"\n{title}\n{'-' * len(title)}")
print("\n".join(card) if card else "No credit card numbers found.")
print('---')



