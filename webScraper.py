import requests
from bs4 import BeautifulSoup, Comment

# URL to scrape
url = 'https://www.example.com/'

# Send a GET request
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of page
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Extract the content between <title></title> 
    title_tag = soup.find('title')
    if title_tag:
        title = title_tag.get_text()
        print(f'Title Tag Content: {title}')
    
    # Extract any commented code or messages
    comments = soup.find_all(string=lambda text: isinstance(text, Comment))
    for i, comment in enumerate(comments):
        print(f'Comment {i + 1}: {comment}')
    
    # Extract any javascript
    scripts = soup.find_all('script')
    for i, script in enumerate(scripts):
        script_content = script.get_text()
        print(f'Script {i + 1} Content: {script_content}')
    
    # Extract content in <h1> tags
    title_tag = soup.find('h1')
    if title_tag:
        title = title_tag.get_text()
        print(f'Article Title: {title}')
    
    # Extract article content
    article_content = ''
    paragraphs = soup.find_all('p')
    for paragraph in paragraphs:
        article_content += paragraph.get_text() + '\n'
        
    links = soup.find_all('link')
    link_content = ''
    for link in links:
        link_content += f'href: {link.get("href")}, rel: {link.get("rel")}, https: {link.get("https")}\n'
    
    print(f'Article Content: {article_content}')
    print(f'Link Content: {link_content}')
else:
    print(f'Failed. Status code: {response.status_code}')