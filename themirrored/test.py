import re

url = "https://youtu.be/wQSbQaSlG6s?si=f76aKaNUrEWnuYt-"
match = re.search(r'youtu.be/([^/]+)', url)

if match:
    result = match.group(1)
    print(result)
else:
    print("No match found.")