# Regex Data Extraction | Onboarding Hackaton
This task challenges one to leverage the power of regular expressions to build a data extraction module.  
**Prologue** - As a newly minted Junior Full Stack Developer fresh out of a three-year program, you've landed a short-term gig to develop a web application for a private organization. Your role involves designing an API that aggregates data from across the web and displays relevant information based on user requests. 

## Project Overview  
Modern web APIs often return massive amounts of unstructured text. So, to efficiently sift through this data, this Data Extractor script is designed to parse and extract key information types, including:  
- [x] **Email Addresses:** Identifies and extracts email addresses.
- [x] **URLs:** Extracts HTTP/HTTPS URLs while avoiding trailing punctuation.
- [x] **Phone Numbers:** Extracts phone numbers in various common formats.
- [x] **Credit Card Numbers:** Extracts credit card numbers formatted with spaces or hyphens.
- [x] **HTML Tags:** Extracts Html tags.
- [x] **Hashtags:** Extracts hashtags in the string. eg - ```#OutreachyInterns```

## Setup and Installation
Ensure you have Python 3 installed, then
- Clone the Repository:
```
git clone https://github.com/Mr-Eke/alu_regex-data-extraction-Mr-EKE.git
```
- Switch to the Project Directory
```
cd alu_regex-data-extraction-Mr-Eke
```
## Dependencies:
This project uses Python's built-in ```re module```, so no additional packages are required.  
## Usage Instructions
- Running the Script:
The repository includes a ```test_cases.py``` script that demonstrates how to use the DataExtractor class with a sample text. To run the script, execute: ⤵️ 
```
python3 test_cases.py
```
## Example Output:
The script will print extracted data under clearly labelled sections. For example: ⤵️  
```
Extracted Emails:
-----------------
support@eke-chi.co.uk
wdebela@alueducation.com
...

Extracted URLs:
-----------------
http://elgibbor.hashnode.dev
https://www.linkedin.com/in/chiago/
...

Extracted Phone numbers:
-----------------
+1234567890
(987) 654-3210
+1-800-555-0199
...
```
## Customizing the Extraction:
- **Modify Input:** Update the ```test_string``` variable in the ```test_cases.py``` script with your own text to test different extraction scenarios.
## Author 🧠
**Chiagoziem Eke** - [Linkedin](https://www.linkedin.com/in/chiago/) | [Blog](http://elgibbor.hashnode.dev) | [Email](c.eke@alustudent.com)
