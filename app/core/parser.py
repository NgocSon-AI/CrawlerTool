from bs4 import BeautifulSoup

class HTMLParser():
     """
     Phân tích HTML bằng BeautifulSoup.
     """

     def parser(self, html: str):
          """
          Chuyển HTML → đối tượng BeautifulSoup
          """
          return BeautifulSoup(html, "html.parser")
     