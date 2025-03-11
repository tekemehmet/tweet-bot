import os

POSTED_NEWS_FILE = "posted_news.txt"

def load_posted_news():
    """Daha önce paylaşılmış haberleri yükler."""
    if not os.path.exists(POSTED_NEWS_FILE):
        return set()
    with open(POSTED_NEWS_FILE, "r", encoding="utf-8") as file:
        return set(line.strip() for line in file.readlines())

def save_posted_news(title):
    """Yeni paylaşılan haberi dosyaya ekler."""
    with open(POSTED_NEWS_FILE, "a", encoding="utf-8") as file:
        file.write(title + "\n")
