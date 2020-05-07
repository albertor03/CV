import json


class Data:

    def get_data(self, path):
        data = self.open_file(path)

        return data

    def get_last_employment(self, path):
        data = self.open_file(path)
        last = list()
        employment = list()

        for items in data:
            for item in items['section']:
                last += item['info'].values()

        employment.append(last[-6])
        employment.append(last[-5])

        return employment

    @staticmethod
    def open_file(path):
        file = open(path, 'r')
        data = json.load(file)
        file.close()

        return data
