# # import time
# # import psycopg2
# # from selenium import webdriver
# # from selenium.webdriver.common.by import By
# # from selenium.webdriver.support.ui import WebDriverWait
# # from selenium.webdriver.support import expected_conditions as EC

# # # PostgreSQL connection
# # conn = psycopg2.connect(
# #     dbname="news_website",
# #     user="postgres",
# #     password="Postgres@94",
# #     host="localhost",
# #     port="5432"
# # )
# # cursor = conn.cursor()

# # # Ensure 'category' column exists
# # cursor.execute("""
# #     ALTER TABLE articles ADD COLUMN IF NOT EXISTS category TEXT;
# # """)
# # conn.commit()

# # # Category mapping
# # category_keywords = {
# #     "politics": ["politics", "election", "government"],
# #     "technology": ["tech", "technology", "innovation"],
# #     "sports": ["sport", "football", "cricket", "olympics"],
# #     "entertainment": ["entertainment", "film", "movie", "music"],
# #     "business": ["business", "market", "finance"],
# #     "health": ["health", "wellness", "medical"],
# #     "world": ["world", "international", "global"],
# #     "science": ["science", "research"],
# #     "education": ["education", "school", "university"],
# # }

# # def identify_category(url, content):
# #     for category, keywords in category_keywords.items():
# #         if any(keyword in url.lower() or keyword in content.lower() for keyword in keywords):
# #             return category
# #     return "general"

# # # Set up Selenium
# # options = webdriver.ChromeOptions()
# # options.add_argument("--headless")
# # options.add_argument("--disable-gpu")
# # driver = webdriver.Chrome(options=options)

# # # BBC News URL
# # bbc_url = "https://www.bbc.com/news"
# # driver.get(bbc_url)

# # print("🔍 Fetching BBC Articles...")

# # wait = WebDriverWait(driver, 15)

# # def get_articles():
# #     return driver.find_elements(By.CSS_SELECTOR, "a[data-testid='internal-link']")

# # articles = get_articles()

# # for i in range(min(10, len(articles))):  # Limit to 10 articles
# #     try:
# #         articles = get_articles()

# #         article = articles[i]
# #         headline = article.text.strip()
# #         source_url = article.get_attribute("href")

# #         if not headline or not source_url:
# #             continue

# #         print(f"📰 Processing: {headline}")

# #         cursor.execute("SELECT 1 FROM articles WHERE source_url = %s", (source_url,))
# #         if cursor.fetchone():
# #             print("🔄 Skipping duplicate article")
# #             continue

# #         driver.get(source_url)
# #         wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
# #         time.sleep(3)

# #         author = driver.find_element(By.CSS_SELECTOR, ".ssrcss-68pt20-Contributor").text if driver.find_elements(By.CSS_SELECTOR, ".ssrcss-68pt20-Contributor") else "Not Available"
# #         publication_date = driver.find_element(By.CSS_SELECTOR, "time").get_attribute("datetime") if driver.find_elements(By.CSS_SELECTOR, "time") else "Not Available"
# #         summary = driver.find_element(By.CSS_SELECTOR, "p.ssrcss-1q0x1qg-Paragraph").text if driver.find_elements(By.CSS_SELECTOR, "p.ssrcss-1q0x1qg-Paragraph") else "Not Available"
# #         content = " ".join([p.text for p in driver.find_elements(By.CSS_SELECTOR, "p")]) if driver.find_elements(By.CSS_SELECTOR, "p") else "Not Available"
# #         image_url = driver.find_element(By.TAG_NAME, "img").get_attribute("src") if driver.find_elements(By.TAG_NAME, "img") else "Not Available"

# #         # Identify category
# #         category = identify_category(source_url, content)

# #         cursor.execute("""
# #             INSERT INTO articles (headline, author, publication_date, summary, content, image_url, source_url, category)
# #             VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
# #             ON CONFLICT (source_url) DO NOTHING;
# #         """, (headline, author, publication_date, summary, content, image_url, source_url, category))

# #         conn.commit()
# #         print(f"✅ Saved: {headline} | Category: {category}")

# #         driver.get(bbc_url)
# #         wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
# #         time.sleep(3)

# #     except Exception as e:
# #         print(f"❌ Error: {e}")
# #         driver.get(bbc_url)
# #         time.sleep(3)

# # driver.quit()
# # cursor.close()
# # conn.close()

# # print("✅ Data scraping completed.")

# # ----------------------------------------------------------------------------------------------------
# import time
# import psycopg2
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# # PostgreSQL connection
# conn = psycopg2.connect(
#     dbname="news_website",
#     user="postgres",
#     password="Postgres@94",
#     host="localhost",
#     port="5432"
# )
# cursor = conn.cursor()

# # Ensure 'category' column exists
# cursor.execute("""
#     ALTER TABLE articles ADD COLUMN IF NOT EXISTS category TEXT;
# """)
# conn.commit()

# # BBC News categories with correct URLs
# bbc_categories = {
#     'business': 'business',
#     'innovation': 'innovation',
#     'culture': 'culture',
#     'arts': 'arts',
#     'travel': 'travel',
#     'politics':'news/politics'
    
# }

# # Set up Selenium
# options = webdriver.ChromeOptions()
# options.add_argument("--headless")
# options.add_argument("--disable-gpu")
# driver = webdriver.Chrome(options=options)

# wait = WebDriverWait(driver, 15)

# # Scroll page function
# def scroll_page():
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#     time.sleep(3)

# def get_articles():
#     return driver.find_elements(By.CSS_SELECTOR, "a[data-testid='internal-link']")

# def scrape_articles(category, path):
#     category_url = f"https://www.bbc.com/news/{path}"
#     driver.get(category_url)
#     print(f"🔍 Fetching articles for category: {category}")

#     articles = get_articles()

#     while True:
#         scroll_page()
#         new_articles = get_articles()
#         if len(new_articles) == len(articles):
#             break
#         articles = new_articles

#     for article in articles:
#         try:
#             source_url = article.get_attribute("href")
#             headline = article.text.strip()

#             if not headline or not source_url:
#                 continue

#             print(f"📰 Processing: {headline}")

#             cursor.execute("SELECT 1 FROM articles WHERE source_url = %s", (source_url,))
#             if cursor.fetchone():
#                 print("🔄 Skipping duplicate article")
#                 continue

#             # Open article in a new tab
#             driver.execute_script("window.open('', '_blank');")
#             driver.switch_to.window(driver.window_handles[1])
#             driver.get(source_url)

#             wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
#             time.sleep(3)

#             author = driver.find_element(By.CSS_SELECTOR, ".ssrcss-68pt20-Contributor").text if driver.find_elements(By.CSS_SELECTOR, ".ssrcss-68pt20-Contributor") else "Not Available"
#             publication_date = driver.find_element(By.CSS_SELECTOR, "time").get_attribute("datetime") if driver.find_elements(By.CSS_SELECTOR, "time") else "Not Available"
#             summary = driver.find_element(By.CSS_SELECTOR, "p.ssrcss-1q0x1qg-Paragraph").text if driver.find_elements(By.CSS_SELECTOR, "p.ssrcss-1q0x1qg-Paragraph") else "Not Available"
#             content = " ".join([p.text for p in driver.find_elements(By.CSS_SELECTOR, "p")]) if driver.find_elements(By.CSS_SELECTOR, "p") else "Not Available"
#             image_url = driver.find_element(By.TAG_NAME, "img").get_attribute("src") if driver.find_elements(By.TAG_NAME, "img") else "Not Available"

#             cursor.execute("""
#                 INSERT INTO articles (headline, author, publication_date, summary, content, image_url, source_url, category)
#                 VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
#                 ON CONFLICT (source_url) DO UPDATE SET
#                     headline = EXCLUDED.headline,
#                     author = EXCLUDED.author,
#                     publication_date = EXCLUDED.publication_date,
#                     summary = EXCLUDED.summary,
#                     content = EXCLUDED.content,
#                     image_url = EXCLUDED.image_url,
#                     category = EXCLUDED.category;
#             """, (headline, author, publication_date, summary, content, image_url, source_url, category))

#             conn.commit()
#             print(f"✅ Saved: {headline} | Category: {category}")

#             # Close the article tab and switch back
#             driver.close()
#             driver.switch_to.window(driver.window_handles[0])

#         except Exception as e:
#             print(f"❌ Error: {e}")
#             driver.close()
#             driver.switch_to.window(driver.window_handles[0])

# # Scrape all categories
# for category, path in bbc_categories.items():
#     scrape_articles(category, path)

# # Close resources
# driver.quit()
# cursor.close()
# conn.close()

# print("✅ Data scraping completed.")




# import time
# import psycopg2
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# # PostgreSQL connection
# conn = psycopg2.connect(
#     dbname="news_website",
#     user="postgres",
#     password="Postgres@94",
#     host="localhost",
#     port="5432"
# )
# cursor = conn.cursor()

# # Ensure 'category' column exists
# cursor.execute("""
#     ALTER TABLE articles ADD COLUMN IF NOT EXISTS category TEXT;
# """)
# conn.commit()

# # BBC News categories with correct URLs
# bbc_categories = {
#     'business': 'business',
#     'innovation': 'innovation',
#     'culture': 'culture',
#     'arts': 'arts',
#     'travel': 'travel',
#     'politics': 'news/politics'
# }

# # Set up Selenium
# options = webdriver.ChromeOptions()
# options.add_argument("--headless")
# options.add_argument("--disable-gpu")
# driver = webdriver.Chrome(options=options)

# wait = WebDriverWait(driver, 15)

# # Scroll page function
# def scroll_page():
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#     time.sleep(3)

# def get_articles():
#     return driver.find_elements(By.CSS_SELECTOR, "a[data-testid='internal-link']")

# def scrape_articles(category, path):
#     category_url = f"https://www.bbc.com/news/{path}"
#     driver.get(category_url)
#     print(f"🔍 Fetching articles for category: {category}")

#     articles = get_articles()

#     while True:
#         scroll_page()
#         new_articles = get_articles()
#         if len(new_articles) == len(articles):
#             break
#         articles = new_articles

#     for article in articles:
#         try:
#             source_url = article.get_attribute("href")
#             headline = article.text.strip()

#             if not headline or not source_url:
#                 continue

#             print(f"📰 Processing: {headline}")

#             cursor.execute("SELECT 1 FROM articles WHERE source_url = %s", (source_url,))
#             if cursor.fetchone():
#                 print("🔄 Skipping duplicate article")
#                 continue

#             # Open article in a new tab
#             driver.execute_script("window.open('', '_blank');")
#             driver.switch_to.window(driver.window_handles[1])
#             driver.get(source_url)

#             wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
#             time.sleep(1)

#             author = driver.find_elements(By.CSS_SELECTOR, ".ssrcss-68pt20-Contributor").text if driver.find_elements(By.CSS_SELECTOR, ".ssrcss-68pt20-Contributor") else "Not Available"
#             publication_date = driver.find_element(By.CSS_SELECTOR, "time").get_attribute("datetime") if driver.find_elements(By.CSS_SELECTOR, "time") else "Not Available"
#             content = " ".join([p.text for p in driver.find_elements(By.CSS_SELECTOR, "p")]) if driver.find_elements(By.CSS_SELECTOR, "p") else "Not Available"
#             image_url = driver.find_element(By.TAG_NAME, "img").get_attribute("src") if driver.find_elements(By.TAG_NAME, "img") else "Not Available"

#             cursor.execute("""
#                 INSERT INTO articles (headline, author, publication_date, summary, content, image_url, source_url, category)
#                 VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
#                 ON CONFLICT (source_url) DO UPDATE SET
#                     headline = EXCLUDED.headline,
#                     author = EXCLUDED.author,
#                     publication_date = EXCLUDED.publication_date,
#                     content = EXCLUDED.content,
#                     image_url = EXCLUDED.image_url,
#                     category = EXCLUDED.category;
#             """, (headline, author, publication_date, content, image_url, source_url, category))

#             conn.commit()
#             print(f"✅ Saved: {headline} | Category: {category}")

#             # Close the article tab and switch back
#             driver.close()
#             driver.switch_to.window(driver.window_handles[0])

#         except Exception as e:
#             print(f"❌ Error: {e}")
#             driver.close()
#             driver.switch_to.window(driver.window_handles[0])

# # Scrape all categories
# for category, path in bbc_categories.items():
#     scrape_articles(category, path)

# # Close resources
# driver.quit()
# cursor.close()
# conn.close()

# print("✅ Data scraping completed.")

import time
import psycopg2
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# PostgreSQL connection
conn = psycopg2.connect(
    dbname="news_website",
    user="postgres",
    password="Postgres@94",
    host="localhost",
    port="5432"
)
cursor = conn.cursor()

# Ensure 'category' column exists
cursor.execute("""
    ALTER TABLE articles ADD COLUMN IF NOT EXISTS category TEXT;
""")
conn.commit()

# BBC News categories with correct URLs
bbc_categories = {
    'business': 'business',
    'innovation': 'innovation',
    'culture': 'culture',
    'travel': 'travel',
    'politics': 'news/politics'
}


# Set up Selenium
options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
driver = webdriver.Chrome(options=options)

wait = WebDriverWait(driver, 15)

# Scroll page function
def scroll_page():
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

# def get_articles():
#     return driver.find_elements(By.CSS_SELECTOR, "a[data-testid='internal-link']")

# def get_articles():
#     # Regular articles (works for most categories)
#     articles = driver.find_elements(By.CSS_SELECTOR, "a[data-testid='internal-link']")
    
#     # Handle politics section (different structure)
#     if not articles:
#         articles = driver.find_elements(By.CSS_SELECTOR, "div[data-testid='card-text-wrapper']")
    
#     return articles


# def scrape_articles(category, path):
#     category_url = f"https://www.bbc.com/{path}"
#     driver.get(category_url)
#     print(f"🔍 Fetching articles for category: {category}")

#     scroll_page()
#     articles = get_articles()

#     for article in articles:
#         try:
#             source_url = article.get_attribute("href")
#             headline = article.text.strip()

#             if not headline or not source_url:
#                 continue

#             print(f"📰 Processing: {headline}")

#             # cursor.execute("SELECT 1 FROM articles WHERE source_url = %s", (source_url,))
#             # if cursor.fetchone():
#             #     print("🔄 Skipping duplicate article")
#             #     continue

#             # Open article in a new tab
#             driver.execute_script("window.open('', '_blank');")
#             driver.switch_to.window(driver.window_handles[1])
#             driver.get(source_url)

#             wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
#             time.sleep(2)

#             author_elements = driver.find_elements(By.CSS_SELECTOR, ".ssrcss-68pt20-Contributor")
#             author = author_elements[0].text if author_elements else "Not Available"

#             publication_date_element = driver.find_elements(By.CSS_SELECTOR, "time")
#             publication_date = publication_date_element[0].get_attribute("datetime") if publication_date_element else "Not Available"

#             content = " ".join([p.text for p in driver.find_elements(By.CSS_SELECTOR, "p")]) if driver.find_elements(By.CSS_SELECTOR, "p") else "Not Available"

#             image_element = driver.find_elements(By.TAG_NAME, "img")
#             image_url = image_element[0].get_attribute("src") if image_element else "Not Available"

#             cursor.execute("""
#                 INSERT INTO articles (headline, author, publication_date, content, image_url, source_url, category)
#                 VALUES (%s, %s, %s, %s, %s, %s, %s)
#                 ON CONFLICT (source_url) DO UPDATE SET
#                     headline = EXCLUDED.headline,
#                     author = EXCLUDED.author,
#                     publication_date = EXCLUDED.publication_date,
#                     content = EXCLUDED.content,
#                     image_url = EXCLUDED.image_url,
#                     source_url = EXCLUDED.source_url,
#                     category = EXCLUDED.category;
#             """, (headline, author, publication_date, content, image_url, source_url, category))

#             conn.commit()
#             print(f"✅ Saved: {headline} | Category: {category}")

#             # Close the article tab and switch back
#             driver.close()
#             driver.switch_to.window(driver.window_handles[0])

#         except Exception as e:
#             print(f"❌ Error: {e}")
#             driver.close()
#             driver.switch_to.window(driver.window_handles[0])

def scrape_articles(category, path):
    category_url = f"https://www.bbc.com/{path}"
    driver.get(category_url)
    print(f"🔍 Fetching articles for category: {category}")

    scroll_page()
    articles = get_articles()

    for article in articles:
        try:
            # Try to get the URL from the href (for normal articles)
            source_url = article.get_attribute("href")

            # If href is not available (like in politics), click to navigate
            if not source_url:
                driver.execute_script("arguments[0].scrollIntoView();", article)
                article.click()
                time.sleep(2)  # Wait for navigation
                source_url = driver.current_url

            headline = article.text.strip()

            if not headline or not source_url:
                continue

            print(f"📰 Processing: {headline}")

            # Open the article to extract more details
            driver.execute_script("window.open('', '_blank');")
            driver.switch_to.window(driver.window_handles[1])
            driver.get(source_url)

            wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
            time.sleep(2)

            # Extract details
            author_elements = driver.find_elements(By.CSS_SELECTOR, ".ssrcss-68pt20-Contributor")
            author = author_elements[0].text if author_elements else "Not Available"

            publication_date_element = driver.find_elements(By.CSS_SELECTOR, "time")
            publication_date = publication_date_element[0].get_attribute("datetime") if publication_date_element else "Not Available"

            content = " ".join([p.text for p in driver.find_elements(By.CSS_SELECTOR, "p")]) if driver.find_elements(By.CSS_SELECTOR, "p") else "Not Available"

            image_element = driver.find_elements(By.TAG_NAME, "img")
            image_url = image_element[0].get_attribute("src") if image_element else "Not Available"

            cursor.execute("""
                INSERT INTO articles (headline, author, publication_date, content, image_url, source_url, category)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                ON CONFLICT (source_url) DO UPDATE SET
                    headline = EXCLUDED.headline,
                    author = EXCLUDED.author,
                    publication_date = EXCLUDED.publication_date,
                    content = EXCLUDED.content,
                    image_url = EXCLUDED.image_url,
                    source_url = EXCLUDED.source_url,
                    category = EXCLUDED.category;
            """, (headline, author, publication_date, content, image_url, source_url, category))

            conn.commit()
            print(f"✅ Saved: {headline} | Category: {category}")

            # Close the article tab and switch back
            driver.close()
            driver.switch_to.window(driver.window_handles[0])

        except Exception as e:
            print(f"❌ Error: {e}")
            driver.close()
            driver.switch_to.window(driver.window_handles[0])


# Scrape all categories
for category, path in bbc_categories.items():
    scrape_articles(category, path)

# Close resources
driver.quit()
cursor.close()
conn.close()

print("✅ Data scraping completed.")













