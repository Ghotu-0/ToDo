import json


class StoreUtility:

    def __init__(self):
        self.DataStorage = "../assets/data/database.json"

        print("Initialized Todo Database")

    def saveToStore(self, data):
        loaded = self.getDatabase()
        loaded.append(data)
        self.localWrite(loaded)

    def removeFromStoreByIndex(self, index):
        loaded = self.getDatabase()
        if index is not None and index < len(loaded):
            del loaded[index]
        self.localWrite(loaded)

    def removeFromStoreByValue(self, value):
        loaded = self.getDatabase()
        if value and value in loaded:
            loaded.remove(value)
        self.localWrite(loaded)

    def localWrite(self, data):
        file2 = open(self.DataStorage, 'w')
        file2.write(json.dumps(data))
        file2.close()

    def modifyTodoStoreProperty(self,index,option,value):
        loaded = self.getDatabase()
        loaded[index][option] = value;
        self.localWrite(loaded)

    def getDatabase(self):
        file = open(self.DataStorage, 'r')
        loaded = json.load(file)
        file.close()
        return loaded

