import json
from random import randint

import ideas.utils as utils

IDEA_PATH = './ideas/ideas.json'


class Generator:

    def __init__(self, context='general', keys=[]):
        self.idea_path = IDEA_PATH
        self.context = context
        self.rand_items = []

        with open(self.idea_path, 'r') as json_file:
            self.lst = json.load(json_file)

        if len(keys) == 0:
            self.keys = self.lst.keys()
        else:
            self.keys = keys

    def get_keys(self):
        return list(self.keys)

    def export_lst(self):
        temp_lst = json.dumps(self.lst, indent=4)
        f = open(self.idea_path, 'w+')
        f.write(temp_lst)
        f.close()

    def get_rand_item(self, key):
        rand_num = randint(0, (len(self.lst[key]) - 1))
        if self.lst[key][rand_num] in self.rand_items:
            rand_num = randint(0, (len(self.lst[key]) - 1))
        self.rand_items.append(self.lst[key][rand_num])
        return self.lst[key][rand_num]

    def generate(self):
        generated_msg = ''
        for key in self.keys:
            generated_msg += f'{self.get_rand_item(key)} \n'
        self.print_result()
        return generated_msg

    def generate_multiple(self, how_many=None, key='items'):
        for i in range(how_many):
            self.get_rand_item(key)
        self.print_result()

    def print_result(self):
        utils.print_result(self.rand_items, self.context)

    @staticmethod
    def convert_file_to_array(file_location):
        with open(file_location, "r") as file_to_convert:
            file_array = file_to_convert.readlines()

        stripped_array = []
        for item in file_array:
            stripped_array.append(item.strip())
        return stripped_array
