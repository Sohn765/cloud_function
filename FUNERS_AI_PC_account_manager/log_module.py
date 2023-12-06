from time import *
import csv




class Log_module():

    def __init__(self):
        self.tm = localtime(time())
        self.ti = strftime('%Y%m%d%I%M%S', self.tm)
        self.current = self.ti
        file = open(f"log/{self.ti}.txt","w",encoding="UTF-8")
        file.close()

        
        

    def log(self,text):
        tm = localtime(time())
        ti = strftime('%Y-%m-%d %I:%M:%S', tm)

        Text_list = f"[{ti}] {text}"
        file = open(f"log/{self.ti}.txt","a",encoding="UTF-8")
        file.write(Text_list+"\n")
        file.close()
        print(text)
        return Text_list