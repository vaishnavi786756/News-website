# from flask import Flask, jsonify, request
# from flask_cors import CORS
# import psycopg2
# import psycopg2.extras

# app = Flask(__name__)

# # PostgreSQL Database Connection
# def get_db_connection():
#     try:
#         return psycopg2.connect(
#             dbname="news_website",
#             user="postgres",
#             password="Postgres@94",
#             host="localhost",
#             port="5432"
#         )
#     except Exception as e:
#         print(f"Database connection error: {e}")
#         return None

# # Fetch all news articles
# @app.route('/api/news', methods=['GET'])
# def get_news():
#     conn = get_db_connection()
#     if not conn:
#         return jsonify({"error": "Database connection failed"}), 500

#     with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
#         cursor.execute("""
#             SELECT id, headline, author, publication_date, summary, content, image_url, source_url, category
#             FROM articles
#             ORDER BY publication_date DESC
#         """)
#         articles = cursor.fetchall()
#     conn.close()

#     news_list = [dict(article) for article in articles]

#     return jsonify(news_list)

# # Helper function to fetch articles by category
# def fetch_news_by_category(category):
#     conn = get_db_connection()
#     if not conn:
#         return jsonify({"error": "Database connection failed"}), 500

#     print(f"Fetching category: {category}")  # Debugging statement

#     with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
#         cursor.execute("""
#             SELECT id, headline, author, publication_date, summary, content, image_url, source_url, category
#             FROM articles
#             WHERE LOWER(category) = LOWER(%s)
#             ORDER BY publication_date DESC
#         """, (category,))
#         articles = cursor.fetchall()

#     conn.close()

#     if not articles:
#         return jsonify({"error": f"No articles found for category '{category}'"}), 404

#     return jsonify([dict(article) for article in articles])

# # Routes for the specified categories
# @app.route('/api/news/politics', methods=['GET'])
# def get_politics():
#     return fetch_news_by_category('Politics')

# @app.route('/api/news/innovation', methods=['GET'])
# def get_technology():
#     return fetch_news_by_category('innovation')

# @app.route('/api/news/culture', methods=['GET'])
# def get_entertainment():
#     return fetch_news_by_category('culture')

# @app.route('/api/news/travel', methods=['GET'])
# def get_travel():
#     return fetch_news_by_category('travel')

# @app.route('/api/news/arts', methods=['GET'])
# def get_arts():
#     return fetch_news_by_category('arts')

# @app.route('/api/news/business', methods=['GET'])
# def get_business():
#     return fetch_news_by_category('business')

# # Search news articles by keyword
# @app.route('/api/news/search', methods=['GET'])
# def search_news():
#     query = request.args.get('q', '')

#     if not query:
#         return jsonify({"error": "Query parameter 'q' is required"}), 400

#     conn = get_db_connection()
#     if not conn:
#         return jsonify({"error": "Database connection failed"}), 500

#     with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
#         cursor.execute("""
#             SELECT id, headline, author, publication_date, summary, content, image_url, source_url, category
#             FROM articles
#             WHERE headline ILIKE %s OR content ILIKE %s
#             ORDER BY publication_date DESC
#         """, (f"%{query}%", f"%{query}%"))
#         articles = cursor.fetchall()
#     conn.close()

#     if not articles:
#         return jsonify({"error": "No articles matching the search"}), 404

#     return jsonify([dict(article) for article in articles])

# # Fetch detailed news article by ID
# @app.route('/api/news/<int:news_id>', methods=['GET'])
# def get_news_by_id(news_id):
#     conn = get_db_connection()
#     if not conn:
#         return jsonify({"error": "Database connection failed"}), 500

#     with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
#         cursor.execute("""
#             SELECT id, headline, author, publication_date, summary, content, image_url, source_url, category
#             FROM articles
#             WHERE id = %s
#         """, (news_id,))
#         article = cursor.fetchone()
#     conn.close()

#     if article:
#         return jsonify(dict(article))

#     return jsonify({"error": "Article not found"}), 404

# if __name__ == '__main__':
#     app.run(debug=True)




# from flask import Flask, jsonify, request
# from flask_cors import CORS
# import psycopg2
# import psycopg2.extras

# app = Flask(__name__)
# CORS(app)  # Enable CORS for all routes

# # PostgreSQL Database Connection
# def get_db_connection():
#     try:
#         return psycopg2.connect(
#             dbname="news_website",
#             user="postgres",
#             password="Postgres@94",
#             host="localhost",
#             port="5432"
#         )
#     except Exception as e:
#         print(f"Database connection error: {e}")
#         return None

# # Fetch all news articles
# @app.route('/api/news', methods=['GET'])
# def get_news():
#     conn = get_db_connection()
#     if not conn:
#         return jsonify({"error": "Database connection failed"}), 500

#     with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
#         cursor.execute("""
#             SELECT id, headline, author, publication_date, summary, content, image_url, source_url, category
#             FROM articles
#             ORDER BY publication_date DESC
#         """)
#         articles = cursor.fetchall()
#     conn.close()

#     news_list = [dict(article) for article in articles]

#     return jsonify(news_list)

# # Helper function to fetch articles by category
# def fetch_news_by_category(category):
#     conn = get_db_connection()
#     if not conn:
#         return jsonify({"error": "Database connection failed"}), 500

#     print(f"Fetching category: {category}")  # Debugging statement

#     with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
#         cursor.execute("""
#             SELECT id, headline, author, publication_date, summary, content, image_url, source_url, category
#             FROM articles
#             WHERE LOWER(category) = LOWER(%s)
#             ORDER BY publication_date DESC
#         """, (category,))
#         articles = cursor.fetchall()

#     conn.close()

#     if not articles:
#         return jsonify({"error": f"No articles found for category '{category}'"}), 404

#     return jsonify([dict(article) for article in articles])

# # Dynamic route to fetch articles by category
# @app.route('/api/news/category/<string:category>', methods=['GET'])
# def get_category_news(category):
#     return fetch_news_by_category(category)

# # Search news articles by keyword
# @app.route('/api/news/search', methods=['GET'])
# def search_news():
#     query = request.args.get('q', '')

#     if not query:
#         return jsonify({"error": "Query parameter 'q' is required"}), 400

#     conn = get_db_connection()
#     if not conn:
#         return jsonify({"error": "Database connection failed"}), 500

#     with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
#         cursor.execute("""
#             SELECT id, headline, author, publication_date, summary, content, image_url, source_url, category
#             FROM articles
#             WHERE headline ILIKE %s OR content ILIKE %s
#             ORDER BY publication_date DESC
#         """, (f"%{query}%", f"%{query}%"))
#         articles = cursor.fetchall()
#     conn.close()

#     if not articles:
#         return jsonify({"error": "No articles matching the search"}), 404

#     return jsonify([dict(article) for article in articles])

# # Fetch detailed news article by ID
# @app.route('/api/news/<int:news_id>', methods=['GET'])
# def get_news_by_id(news_id):
#     conn = get_db_connection()
#     if not conn:
#         return jsonify({"error": "Database connection failed"}), 500

#     with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
#         cursor.execute("""
#             SELECT id, headline, author, publication_date, summary, content, image_url, source_url, category
#             FROM articles
#             WHERE id = %s
#         """, (news_id,))
#         article = cursor.fetchone()
#     conn.close()

#     if article:
#         return jsonify(dict(article))

#     return jsonify({"error": "Article not found"}), 404

# if __name__ == '__main__':
#     app.run(debug=True)



from flask import Flask, jsonify, request
from flask_cors import CORS
import psycopg2
import psycopg2.extras

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# PostgreSQL Database Connection
def get_db_connection():
    try:
        return psycopg2.connect(
            dbname="news_website",
            user="postgres",
            password="Postgres@94",
            host="localhost",
            port="5432"
        )
    except Exception as e:
        print(f"Database connection error: {e}")
        return None

# Fetch all news articles
@app.route('/api/news', methods=['GET'])
def get_news():
    conn = get_db_connection()
    if not conn:
        return jsonify({"error": "Database connection failed"}), 500

    with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
        cursor.execute("""
            SELECT id, headline, author, publication_date, content, image_url, source_url, category
            FROM articles
            WHERE category IS NOT NULL
            ORDER BY publication_date DESC
        """)
        articles = cursor.fetchall()
    conn.close()

    news_list = [dict(article) for article in articles]

    return jsonify(news_list)

# Helper function to fetch articles by category
def fetch_news_by_category(category):
    conn = get_db_connection()
    if not conn:
        return jsonify({"error": "Database connection failed"}), 500

    print(f"Fetching category: {category}")  # Debugging statement

    with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
        cursor.execute("""
            SELECT id, headline, author, publication_date, content, image_url, source_url, category
            FROM articles
            WHERE LOWER(category) = LOWER(%s) AND category IS NOT NULL
            ORDER BY publication_date DESC
        """, (category,))
        articles = cursor.fetchall()

    conn.close()

    if not articles:
        return jsonify({"error": f"No articles found for category '{category}'"}), 404

    return jsonify([dict(article) for article in articles])

# Dynamic route to fetch articles by category
@app.route('/api/news/category/<string:category>', methods=['GET'])
def get_category_news(category):
    return fetch_news_by_category(category)

# Search news articles by keyword
@app.route('/api/news/search', methods=['GET'])
def search_news():
    query = request.args.get('q', '')

    if not query:
        return jsonify({"error": "Query parameter 'q' is required"}), 400

    conn = get_db_connection()
    if not conn:
        return jsonify({"error": "Database connection failed"}), 500

    with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
        cursor.execute("""
            SELECT id, headline, author, publication_date, content, image_url, source_url, category
            FROM articles
            WHERE (headline ILIKE %s OR content ILIKE %s) AND category IS NOT NULL
            ORDER BY publication_date DESC
        """, (f"%{query}%", f"%{query}%"))
        articles = cursor.fetchall()
    conn.close()

    if not articles:
        return jsonify({"error": "No articles matching the search"}), 404

    return jsonify([dict(article) for article in articles])

# Fetch detailed news article by ID
@app.route('/api/news/<int:news_id>', methods=['GET'])
def get_news_by_id(news_id):
    conn = get_db_connection()
    if not conn:
        return jsonify({"error": "Database connection failed"}), 500

    with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
        cursor.execute("""
            SELECT id, headline, author, publication_date, content, image_url, source_url, category
            FROM articles
            WHERE id = %s AND category IS NOT NULL
        """, (news_id,))
        article = cursor.fetchone()
    conn.close()

    if article:
        return jsonify(dict(article))

    return jsonify({"error": "Article not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)