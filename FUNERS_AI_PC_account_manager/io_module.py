import csv
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

class CSVModule():

    def __init__(self):
        self.cred = credentials.Certificate("just-test-tutorials-firebase-adminsdk-jt9n3-5af427c0c9.json")
        firebase_admin.initialize_app(self.cred)
        self.db = firestore.client()

    def write(self,selet,account,key,owner,category,memo):
        # file = open("text.txt","a",encoding="UTF-8")
        # file.write(account+",")
        # file.write(key+",")
        # file.write(owner+",")
        # file.write(category+",")
        # file.write(memo+"\n")
        # file.close()

        doc_ref = self.db.collection(selet).document(account)
        doc_ref.set({
            u'keyCount': key,
            u'owner' : owner,
            u'purpose': category,
            u'note': memo,
        })

    def read(self):
        # list = []
        # with open("text.txt", 'r',encoding="UTF-8") as file:
        #     reader = csv.reader(file, delimiter=',')
        #     for row in reader:
        #         list.append(row)
        # return list
        lists = []
        select = ["auth","block"]
        for i in select:
            docs = self.db.collection(i).stream()
            lines = []
            for doc in docs:
                use = 0
                collections = self.db.collection(i).document(doc.id).collections()
                for collection in collections:
                    for keyuse in collection.stream():
                        use+=1
                lines.append([doc.id, doc.get('keyCount'),doc.get('owner'),doc.get('purpose'),doc.get('note'),use])
            lists.append(lines)
        return lists

    
    def modify(self,selet,account, key, owner, category, memo):
        # list = []
        # with open("text.txt", 'r',encoding="UTF-8") as file:
        #     reader = csv.reader(file, delimiter=',')
        #     for row in reader:
        #         list.append(row)
                
        # lines = list
        # for line in list:
        #     if  line[0] == select:
        #             list[index] = change
        # file.close()
        # file = open('text.txt','w',newline='',encoding="UTF-8")
        # wr = csv.writer(file)
        # wr.writerows(lines)
        # file.close()

        doc_ref = self.db.collection(selet).document(account)
        doc_ref.set({
            u'keyCount': key,
            u'owner' : owner,
            u'purpose': category,
            u'note': memo,
        })


    def delete(self, select,field):
        # list = []
        # with open("text.txt", 'r',encoding="UTF-8") as file:
        #     reader = csv.reader(file, delimiter=',')
        #     for row in reader:
        #         list.append(row)
        #     file.close()

        # lines = list
        # for line in lines:
        #     if line[0] == select:
        #         list.remove(line)


        # file = open('text.txt','w',newline='',encoding="UTF-8")
        # wr = csv.writer(file)
        # wr.writerows(lines)
        # file.close()

        self.db.collection(select).document(field).delete()

    def offlineseve(self):
        file = open("text.csv","a",encoding="UTF-8")
        lines = self.read()
        for i in lines:
            for j in i:
                file.write(str(j)+",")
            file.write("\n")
    
    def loginCheck(self):
        docs = self.db.collection(u'user').stream()
        for doc in docs:
            print(doc)
    
    def useReset(self,selet,field):
        collections = self.db.collection(selet).document(field).collections()
        for collection in collections:
            for doc in collection.stream():
                self.db.collection(selet).document(field).collection('keys').document(doc.id).delete()


if __name__ == "__main__" :
    module = CSVModule()

    module.delete(str(1))