# *_*coding:utf-8 *_*
class Outputer(object):
    def __init__(self):
        self.data = []

    def collect_data(self, page_url,data):
        if page_url is None or data is None or len(data) <= 0:
            return None
        self.data.append(data)


    def save_to_file(self):
         print(self.data)



