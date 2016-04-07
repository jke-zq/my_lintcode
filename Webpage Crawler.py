import threding
import Queue
import urlparse

# def webCrawler(queue, result):
# 	while True:
# 		url = queue.get()
# 		url = urlpase.urlpase(url)
# 		if url not in result and url.hostname.endswith('wikipidia.org'):
#           result.add(url)
# 			urls = HtmlHelper.parseUrls(url)
# 			for u in urls:
# 				queue.put(u)
# 		queue.task_done()


# if __name__ == '__main__':
# 	total = 10
# 	threadpool = [None] * total
# 	queue = Queue.Queue()
# 	result = set()
# 	for i in range(total):
# 		threadpool[i] = threading.Thread(target = webCrawler, args = (queue, result))
# 		threadpool[i].deamon = True
# 		threadpool[i].start()

#     queue.put('')
#     queue.join()
#     return list(result)

## usign class
queue = Queue.Queue()
result = set()
class WebCrawler(threading.Thread):
	"""docstring for webCrawler"""
	# def __init__(self, arg):
	# 	super(webCrawler, self).__init__()
	# 	self.arg = arg
	def run(self):
		global queue, result
		while True:
			url = queue.get()
			if url not in result and urlParse.urlParse(url).hostname.endswith('wikipidia.org'):
				for u in htmlHelper.parseUrls(url):
					queue.put(u)
				result.add(url)
			queue.task_done()

class Solution(object):
	"""docstring for Solution"""
	# def __init__(self, arg):
	# 	super(Solution, self).__init__()
	# 	self.arg = arg
	def crawler(self, url):
		global queue, result
		total = 10
		thread_pool = [None] * total
		for i in range(total):
			thread_pool[i] = WebCrawler()
			thread_pool[i].deamon = True
			thread_pool[i].start()
		queue.put(url)
		queue.join()
		return list(result)



