class DataExtractor():
     """
     Trích xuất dữ liệu từ cây HTML (ví dụ: tiêu đề, liên kết, đoạn text).
     """

     def extract(self, soup):
          data = []
          for link in soup.fill_all("a", href=True):
               title = link.text.strip()
               href = link["href"]
               if title:
                    data.append({"title": title, "url": href})

          return data