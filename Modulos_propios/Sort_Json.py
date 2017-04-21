from bson import ObjectId
from decimal import *

c = getcontext()
c.traps[FloatOperation] = True


class Sort():

    def sort_list(self, list, type):
        return self.sort_split(list, 0, len(list)-1, type)

    def sort_split(self, list, first, last_one, type):
        if first<last_one:

            split = self.sort_division(list, first, last_one, type)

            self.sort_split(list, first, split -1, type)

            self.sort_split(list, split + 1, last_one, type)

        return list


    def sort_division(self, list, first, last_one, type):


        compare_value = list[first].get(type)

        left_part = first + 1
        right_part = last_one

        done = False

        while not done:

            value_1 = list[left_part].get(type)
            while left_part <= right_part and value_1 <= compare_value:
                left_part += 1
                if left_part < len(list):
                    value_1 = list[left_part].get(type)

            value_2= list[right_part].get(type)
            while  value_2>= compare_value and right_part >= left_part:
                right_part -= 1
                if right_part < len(list):
                    value_2 = list[right_part].get(type)
                    print(value_2)


            if right_part < left_part:
                done = True

            else:
                temporary = list[left_part]
                list[left_part] = list[right_part]
                list[right_part] = temporary

        temporary = list[first]
        list[first] = list[right_part]
        list[right_part] = temporary

        return right_part

