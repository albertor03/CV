import json
import requests


class Data:

    @staticmethod
    def get_data(path):
        x = requests.get(path).text

        data = json.loads(x.replace("null,", ""))

        return data

    def get_last_employment(self, path):
        data = self.get_data(path)
        last = list()
        employment = list()

        for items in data:
            for item in items['section']:
                last += item.values()

        employment.append(last[-2])
        employment.append(last[-5])

        return employment
