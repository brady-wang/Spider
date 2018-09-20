# *_*coding:utf-8 *_*
<<<<<<< HEAD
import pymysql
class Outputer(object):
    def __init__(self):
        self.conn  = pymysql.connect(host='120.79.172.45', user='root', passwd='aa5421010', db='spider')
        self.cur = self.conn.cursor()

    def collect_data(self, page_url,data):
        if page_url is None or data is None or len(data) <= 0 :
            return None
        if  data['url'] is None or data['title'] is None:
            return None

        if len(data['title']) <= 0 or len(data['url']) <= 0:
            return None

        self.save_to_mysql(data)

    def save_to_mysql(self,data):
        import time
        # 格式化成2016-03-20 11:45:39形式
        now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())



        # 插入数据
        sql = "insert ignore into imgs_7160(title,url,create_time) values('{}','{}','{}')".format(data['title'],data['url'],now)
        print(sql)
        reCount = self.cur.execute(sql)
        self.conn.commit()


    def __del__(self):
        self.cur.close()
        self.conn.close()
=======
class Outputer(object):
    def __init__(self):
        self.data = []

    def collect_data(self, page_url,data):
        if page_url is None or data is None or len(data) <= 0:
            return None
        self.data.append(data)



    def save_to_file(self):
         print(self.data)
         fout = open('output.html','w',encoding='utf-8');
         fout.write('<html><head><meta charset="utf-8"></head>')
         for item in self.data:
             fout.write("<a href = '%s' target='_blank'> %s </a>" % ( item['url'], item['title'] ))
             fout.write("<p> %s </p>" % item['desc'])
         fout.write("</body></html>")
>>>>>>> 069d225b498d4ce3c199324fad03bb6a2ee1d884







