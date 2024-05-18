import requests
from bs4 import BeautifulSoup
from collections import Counter

r = requests.get('https://www.poornima.org/')
r_content = r.text

soup = BeautifulSoup(r_content, 'html.parser')
hyperlinks = [a['href'] for a in soup.find_all('a', href=True)]
hyperlink_freq = Counter(hyperlinks)
sorted_hyperlink_freq = sorted(hyperlink_freq.items(), key=lambda x: x[1], reverse=True)
for link, freq in sorted_hyperlink_freq:
    print(f'Hyperlink: {link}\nFrequency: {freq}\n')