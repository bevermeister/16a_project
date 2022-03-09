class checkDouble():
    '''
    a class to check whether a guess has repeated letters

    Attributes: guess: a string, the user's inputted guess
    result: a list; 0 if the letter is not in the word, 1 if it is in the wrong place, 2 if it's in the right place
    count: a dict, meant to store the number of times each letter in guess appears
    repeated: an int, the number of times a letter is repeated (0 if the letter appears only once)
    res_list: a list, stores the result of any repeated letters
    '''
    def __init__(self, guess = str, result = list):
        self.guess = guess
        self.result = result
        self.count = {}
        self.repeated = 0
        self.res_list = []

    def get_count_dict(self):
        '''
        updates self.count with the number of times each letter in guess appears
        args: self
        returns: self.count
        '''
        for i in self.guess:
            if i in self.count:
                self.count[i] += 1
            else:
                self.count[i] = 1
        return self.count
    
    def get_repeated(self):
        '''
        updates self.repeated if any letter in guess appears more than once
        args: self
        returns: self.repeated
        '''
        for i in self.count:
            if self.count[i] > 1:
                self.repeated = i
        return self.repeated

    def update_res_list(self):
        '''
        update self.res_list with the result of any repeated letter
        args: self
        returns: none
        '''
        if self.repeated != 0:
            for j in range(len(self.guess)):
                if self.guess[j] == self.repeated:
                    self.res_list.append(self.result[j])

    def update_result(self):
        '''
        update self.result with the max result value for each letter
        args: self
        returns: none
        '''
        if len(self.res_list) > 0: # change the result of repeated letters to the highest value
            for i in range(len(self.result)):
                if self.guess[i] == self.repeated:
                    self.result[i] = max(self.res_list)