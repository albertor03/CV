import json


class Data:

    @staticmethod
    def get_data(path):
        file = open(path, 'r')
        data = json.load(file)
        file.close()

        return data
