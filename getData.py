import json
import requests

class Data:

    def get_data(self, path):
        data = self.open_file(path)

        return data

    def get_last_employment(self, path):
        data = self.get_data_url(path)
        last = list()
        employment = list()

        for items in data:
            for item in items['section']:
                last += item.values()

        employment.append(last[-2])
        employment.append(last[-5])

        return employment

    @staticmethod
    def open_file(path):
        file = open(path, 'r')
        data = json.load(file)
        file.close()

        return data

    @staticmethod
    def get_data_url(path):
        x = requests.get(path).text

        data = json.loads(x.replace("null,", ""))

        return data
