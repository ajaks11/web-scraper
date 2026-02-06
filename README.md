# 🕷️ Simple Python Web Scraper (Interview Project)

A clean, modular web scraper built with Python to demonstrate **HTTP requests**, **HTML parsing**, and **SQL database integration**. 

Designed as a portfolio project/interview implementation task to show best practices like modular code structure and error handling without using heavy frameworks like Scrapy.

##  Features

-   **Modular Design**: Separation of concerns between scraping logic, database management, and execution.
-   **SQL Integration**: Automatically creates and stores data in a local `SQLite` database (zero configuration required).
-   **Adaptable Parsing**: Includes examples for scraping both a sandbox quote site and **Hacker News**.
-   **Live Feedback**: Prints real-time "highlights" to the console while running.

##  Tech Stack

-   **Python 3.x**
-   **Requests**: For handling HTTP requests.
-   **BeautifulSoup4**: For parsing HTML DOM.
-   **SQLite3**: Built-in Python library for database interaction.

##  Installation

1.  Clone the repository:
    ```bash
    git clone https://github.com/yourusername/interview-scraper.git
    cd interview-scraper
    ```

2.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

##  Usage

Run the main script to start scraping:

```bash
python main.py
```

By default, it scrapes **quotes.toscrape.com**. 

### Switching Sites
To scrape **Hacker News** instead:
1.  Open `main.py`.
2.  Comment out `OPTION A`.
3.  Uncomment `OPTION B`.
4.  Run `python main.py` again.

## 📂 Project Structure

```text
interview_scraper/
├── database_manager.py   # Handles SQLite connection and inserting data
├── scraper.py           # Contains fetching and parsing logic
├── main.py              # Entry point: joins scraper and database
├── requirements.txt     # Python dependencies
└── README.md            # This file
```

## 📝 Example Output

```text
🚀 Starting scraper for: http://quotes.toscrape.com

📥 Fetching page content...
🔍 Parsing highlights...
✅ Found 10 items. Saving to database and displaying highlights:

--------------------------------------------------
📄 HIGHLIGHT: The world as we have created it is a process of our thinking...
   Source: Albert Einstein
   Tags: change, deep-thoughts, thinking, world
--------------------------------------------------

✅ Scraping complete. Data saved to 'scraped_data.db'.
```

## 🤝 Contributing

Feel free to fork this project and add parsers for new sites!
