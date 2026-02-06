import requests
from bs4 import BeautifulSoup

def fetch_page(url):
    """
    Fetches the HTML content of the given URL.
    """
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        } # Mimic a browser to avoid being blocked by some sites
        response = requests.get(url, headers=headers)
        response.raise_for_status() # Raise an error for bad status codes
        return response.text
    except requests.RequestException as e:
        print(f"❌ Error fetching {url}: {e}")
        return None

def parse_quotes_site(html):
    """
    Specific parsing logic for quotes.toscrape.com.
    Returns a list of dictionaries with 'content', 'source', and 'tags'.
    
    IMPORTANT for INTERVIEW:
    To adapt this for a NEWS site:
    1. Inspect the news website (Right click -> Inspect).
    2. Find the HTML tag that holds the headline (e.g., <h2 class="title">).
    3. Change 'soup.find_all' below to match that tag.
    """
    soup = BeautifulSoup(html, 'html.parser')
    items = []
    
    # Selecting all quote containers
    quotes = soup.find_all('div', class_='quote') 
    
    for quote in quotes:
        # 1. Extract the main text (The "Highlight")
        text = quote.find('span', class_='text').get_text(strip=True)
        
        # 2. Extract the source (Author)
        author = quote.find('small', class_='author').get_text(strip=True)
        
        # 3. Extract tags (Keywords)
        tags_list = [tag.get_text() for tag in quote.find_all('a', class_='tag')]
        tags_str = ", ".join(tags_list)
        
        items.append({
            'content': text,
            'source': author,
            'tags': tags_str
        })
        
    return items

def parse_hacker_news(html):
    """
    Real-world example: Parsing Hacker News (news.ycombinator.com).
    Structure:
    - Each story is in a <tr class="athing">...</tr>
    - The title and link are in <span class="titleline"> <a href="...">Title</a> </span>
    """
    soup = BeautifulSoup(html, 'html.parser')
    items = []
    
    # 1. Find all rows that contain valid stories
    rows = soup.find_all('tr', class_='athing')
    
    for row in rows:
        try:
            # 2. Extract the title element
            title_line = row.find('span', class_='titleline')
            if not title_line: continue
            
            link_tag = title_line.find('a')
            text = link_tag.get_text(strip=True)
            link = link_tag['href']
            
            # 3. For 'source', we'll just use the domain or 'HackerNews'
            # (Getting the author requires checking the *next* row, which is tricky but doable.
            # For simplicity, we'll store the link as the source)
            
            items.append({
                'content': text,
                'source': link,
                'tags': 'tech, news'
            })
        except AttributeError:
            continue
            
    return items
