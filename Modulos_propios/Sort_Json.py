class Sort():

    def sort_list(self, list, tipo):
        return self.sort_split(list, 0, len(list)-1, tipo)

    def sort_split(self, list, first, last_one, tipo):
        if first<last_one:

            split = self.sort_division(list, first, last_one, tipo)

            self.sort_split(list, first, split -1, tipo)

            self.sort_split(list, split + 1, last_one, tipo)

        return list


    def sort_division(self, list, first, last_one, tipo):

        compare_value = list[first].get(tipo)

        left_part = first + 1
        right_part = last_one

        done = False

        while not done:
            while left_part <= right_part and list[left_part].get(tipo)<= compare_value:
                left_part +=1

            while list[right_part].get(tipo) >= compare_value and right_part >= left_part:
               right_part -=1

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

'''
lista = [14, 17, 13, 15, 15, 10, 3, 16, 9, 3]
clase = Sort()
data = clase.sort_list(lista, )
print(data)
'''