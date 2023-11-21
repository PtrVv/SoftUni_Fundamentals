# Regex to extract links from text
import re

text_links = input()

pattern = r"(?i)(www.([A-Za-z0-9\-]+)(\.[a-z]+)+)\b"
while text_links:

    matches = re.findall(pattern, text_links)
    for link in matches:
        print("".join(link[0]))
    text_links = input()
    
