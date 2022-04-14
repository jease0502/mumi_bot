import pymongo

class MongoDB (object):
    def __init__(self) -> None:
        self.myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        self.data = self._init_get_data()

    def _init_get_data(self):
        mydb = self.myclient["mumi_msg"]
        collection = mydb["msg"]
        return collection

    def get_data(self , msg):
        if msg in self.data[msg]:
            return self.data[msg]
        else:
            print("查無此資料")
            return None

    def insert_data(self, answer , question):
        self.data.insert_one({answer : question})
        if(self.get_data(answer) == question):
            return True
        else:
            return False

    def delete_data(self, answer , question):
        self.data.delete_one({answer : question})
        if(self.get_data(answer) == None):
            return True
        else:
            return False

    def update_data(self, answer , question):
        self.data.update_one({answer : question})
        if(self.get_data(answer) == question):
            return True
        else:
            return False