class Check:
    def __int__(self):
        self.numbers = None

    secret_nums = [2, 4, 6, 8]
    def checker_list(self, nums):
        try:
            numbers = [int(s) for s in nums]
            if len(numbers) != 4:
                response_line = "The amount of digits should be equal to 4"
                return response_line
            if len(numbers) != len(set(numbers)):
                response_line = "The value should be unique"
                return response_line
            for i in numbers:
                if i > 9 or i < 1:
                    response_line = "The digits must be bigger than 0 and less then 10"
                    return response_line
            self.numbers = numbers

        except ValueError:
            response_line = "Please write integers"
            return response_line

    def get_result(self):
        bulls = 0
        cows = 0
        for i in range(len(self.numbers)):
            if self.numbers[i] == self.secret_nums[i]:
                bulls += 1
            elif self.numbers[i] in self.secret_nums:
                cows += 1
        if bulls == 4:
            response_line = "You win"
            return response_line
        else:
            print(bulls)
            print(cows)
            response_line = f'You have {bulls} bulls and {cows} cows'
            return response_line

    def counter(self):
        return step += 1
