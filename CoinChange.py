class Solution:
    map = dict()
    coins = []

    def coinChange(self, coins, amount) -> int:
        self.coins = coins
        result = self.dynamic_programming(amount)
        if amount == 0:
            return 0
        elif result == 255:
            return -1
        else:
            return result

    def dynamic_programming(self, sum):
        if sum in self.coins:
            self.map[sum] = 1
            return 1
        elif sum < min(self.coins):
            return 2 ** 8 - 1

        if not (sum in self.map):
            self.map[sum] = 255
            for coin in self.coins:
                self.map[sum] = min(self.map[sum], self.dynamic_programming(sum - coin) + 1)
        return self.map[sum]


if __name__ == '__main__':
    solution = Solution()
    print(solution.coinChange([2], 3))
