class Check:

    def checker_list(self, get_nums):
        if len(get_nums) == 4:
            if len(get_nums) == len(set(get_nums)):
                for i in get_nums:
                    if 0 < i < 10:
                        return get_nums
                    else:
                        raise ValueError
            else:
                raise ValueError
        else:
            raise ValueError

    def checker_game(self, get_nums, secret_nums):
        # secret_nums = [2, 4, 6, 8]

        pass
