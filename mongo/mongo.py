import pymongo

class MongoDB (object):
    def __init__(self) -> None:
        self.myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        self.data = self._init_get_data()

    def _init_get_data(self):
        self.mydb = self.myclient["mumi_msg"]["msg"]
        collection = self.mydb["msg"].find_one()
        return collection

    def get_data(self , msg):
        try :
            recall = self.data[msg]
            return recall
        except :
            return False

    def insert_data(self, answer , question):
        self.mydb.insert_one({answer : question})
        if(self.get_data(answer) == question):
            return True
        else:
            return False

    def delete_data(self, answer , question):
        self.mydb.delete_one({answer : question})
        if(self.get_data(answer) == None):
            return True
        else:
            return False

    def update_data(self, answer , question):
        self.mydb.update_one({answer : question})
        if(self.get_data(answer) == question):
            return True
        else:
            return False