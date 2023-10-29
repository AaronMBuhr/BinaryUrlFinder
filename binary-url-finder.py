import re
import sys

# Define a regular expression pattern for URLs
url_pattern = re.compile(
    r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
)

# Open the binary file
with open(sys.argv[1], 'rb') as file:
    # Read the file content
    content = file.read()
    
    # Handle invalid utf-8 sequences by replacing them
    content_str = content.decode('utf-8', errors='replace')
    
    # Find all URLs using the regular expression pattern
    urls = set(re.findall(url_pattern, content_str))
    
    # Print the extracted URLs
    for url in urls:
        print(url)

