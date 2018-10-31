import feedparser

class RssFeed:
	news_entries = {}
	def __init__(self, rss_urls):
		for url in rss_urls:
			news = feedparser.parse(url)
			feed_entries = []
			for entry in range(0, len(news.entries)):
				feed_entries.append({ 'title': news.entries[entry].title, 'author': news.entries[entry].author })
			
			self.news_entries[news.feed.title] = feed_entries
			

