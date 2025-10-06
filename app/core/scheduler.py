class Schedular():
     """
     Quản lý hàng đợi URL (tối giản).
     """
     def __init__(self, urls):
          self.queue = list(urls)

     def has_next(self):
          return len(self.queue) > 0
     def next_url(self):
          return self.queue.pop(0)