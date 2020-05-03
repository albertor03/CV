import json


class Data:

    @staticmethod
    def get_data():
        file = open('data/info.json', 'r')
        data = json.load(file)
        file.close()

        return data
