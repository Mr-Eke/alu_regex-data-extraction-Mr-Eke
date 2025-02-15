#!/usr/bin/env python3

from typing import Callable, Dict
from data_extractor import DataExtractor

# Sample text/string to extract relevant data from
test_string = """
    ======= Edge Cases: Invalid Email Addresses ========
    "very.unusual.@.unusual.com"@example.com
    "user\\\"name"@example.com user@[192.168.1.1]
    My email is user(at)example.com user@@example.com user@example..com.
    user@, user.example.com  # (Invalid: missing @)
    example.emailaddress.com  # (Invalid: looks like a domain, not an email)
    "email": "user@example,com"  # (Invalid: comma instead of dot)

    ============ Valid Email Addresses =============
    eke-chi.me@example.co.uk alt email: eke101.c@alustudent.com
    Contact me at c.eke@alustudent.com and for any support inquiries,
    reach out to support@alueducation.com. emails in bracket (braces@example.org)

     ========= Edge Cases: Invalid URLs (Not Matched) =========
        "http:/example.com",        - Missing slash
        "https//example.com",       - Missing colon
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

    ========== Edge Cases: Phone numbers (Different formats) =========
    (123) 456-7890 or call this number 123-456-7890
    123.456.7890.
    you can reach Herve at +250788899944, +1 123-456-7890.

    ==================== credit Card =====================
    1234 5678 9012 3456,1234-5678-9012-3456
    Invalid (Morethan a credit card lenght): 1234-5678-9012-345655

    ==================== Valid Time Formats =====================
    14:30 02:30 pm, 01:30 am - 03:01AM*04:01 PM

    ============ Invalid Time formats (Not matched) ============
     15:60 24:30  2: 20,  5:10  PM, 01:30  am

     ========= HTML tags: ========
    <p><div class="example">, <img src="image.jpg" alt="description"/>

    ============== Hashtags: ==============
    #example #ThisIsAHashtag-#AluSWE

    ========== Currency amounts: ===========
    $19.99 $1,234.56
"""

# creat an instance of DataExtractor with the sample string
extractor: DataExtractor = DataExtractor(test_string)

# Map section titles to their respective extraction functions
extractors: Dict[str, Callable[[], list[str]]] = {
    "Extracted URLs:": extractor.extract_urls,
    "Extracted Hashtags": extractor.get_hashtags,
    "Extracted Emails:": extractor.extract_emails,
    "Extracted Html Tags": extractor.get_html_tags,
    "Extracted Time Formats:": extractor.extract_time,
    "Extracted Phone Numbers:": extractor.extract_phone_numbers,
    "Extracted Currency Amounts": extractor.get_currency_amounts,
    "Extracted Credit Card Numbers:": extractor.extract_credit_cards,
}

# Loop through each extraction method and print the results
for title, extract_func in extractors.items():
    print(f"\n{title}\n{'-' * len(title)}")  # prints a line
    results = extract_func()
    print("\n".join(results) if results else f"No {title.split()[1].lower()} found.")
    print('---')
