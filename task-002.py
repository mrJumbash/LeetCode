class Solution:
    def fizzBuzz(self, n: int):
        list_ = []
        for i in range(1, n+1):
            if i % 3 == 0 and i % 5 == 0:
                list_.append("FizzBuzz")

            elif i % 3 == 0:
                list_.append("Fizz")

            elif i % 5 == 0:
                list_.append("Buzz")

            else:
                list_.append(str(i))

        return list_
