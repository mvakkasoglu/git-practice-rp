# Created by Leon Hunter at 12:10 PM 12/08/2020
class Lister(object):
    def get_integer_list(self, start, stop, step):
        ''' TODO - Implement solution
        Given 3 integers,
            `start`, `stop`, and `step`
        return a list of all integers
            between `start`,
            incrementing by `step`,
            up to and including `stop`
        '''
        list = []
        if step != 0:
            for i in range(start, stop+1, step):
                list.append(i)
        else :
            list = [stop]

        return list

    def get_even_list(self, start, stop, step):
        ''' TODO - Implement solution
        Given 3 integers,
            `start`, `stop`, and `step`
        return a list of all integers
            between `start`,
            incrementing by `step`,
            up to and including `stop`
            and are divisible by 2
        '''
        list = []
        for i in self.get_integer_list(start, stop, step):
            if i % 2 == 0:
                list.append(i)

        # list = []
        # if step != 0:
        #     for i in range(start, stop + 1, step):
        #         if i % 2 ==0:
        #             list.append(i)
        # else:
        #     list = [stop]
        #
        return list

    def get_odd_list(self, start, stop, step):
        ''' TODO - Implement solution
        Given 3 integers,
            `start`, `stop`, and `step`
        return a list of all integers
            between `start`,
            incrementing by `step`,
            up to and including `stop`
            and are not divisible by 2
        '''
        list = []
        for i in self.get_integer_list(start, stop, step):
            if i % 2 != 0:
                list.append(i)
        return list
