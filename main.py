from database_manager import create_database, save_highlight, close_connection
from scraper import fetch_page, parse_quotes_site

from scraper import fetch_page, parse_quotes_site, parse_hacker_news

def main():
    # ---------------------------------------------------------
    # CONFIGURATION: Choose your target
    # ---------------------------------------------------------
    # OPTION A: Practice Site
    SITE_CONFIG = {
        'url': "http://quotes.toscrape.com",
        'parser': parse_quotes_site
    }
    
    # OPTION B: Live Site (Uncomment to use)
    # SITE_CONFIG = {
    #     'url': "https://news.ycombinator.com/",
    #     'parser': parse_hacker_news
    # }
    # ---------------------------------------------------------

    print(f"🚀 Starting scraper for: {SITE_CONFIG['url']}\n")

    # 2. Database Setup
    conn = create_database()
    if not conn:
        return

    # 3. Fetch Data
    print("📥 Fetching page content...")
    html = fetch_page(SITE_CONFIG['url'])
    
    if html:
        # 4. Parse Data
        print("🔍 Parsing highlights...")
        
        # We call the parser function chosen in SITE_CONFIG
        data = SITE_CONFIG['parser'](html)
        
        print(f"✅ Found {len(data)} items. Saving to database and displaying highlights:\n")
        print("-" * 50)
        
        # 5. Save and Display
        for item in data:
            # Save to SQL
            save_highlight(conn, item['content'], item['source'], item['tags'])
            
            # Display
            print(f"📄 HIGHLIGHT: {item['content']}")
            print(f"   Source: {item['source']}")
            print(f"   Tags: {item['tags']}")
            print("-" * 50)
            
        print("\n✅ Scraping complete. Data saved to 'scraped_data.db'.")
    
    close_connection(conn)

if __name__ == "__main__":
    main()
