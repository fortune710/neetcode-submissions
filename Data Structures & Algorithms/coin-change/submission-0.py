class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = {}
        n = len(coins)

        def pickCoin(remaining_amount: int):
            if remaining_amount == 0:
                return 0

            if remaining_amount < 0:
                return float('inf')

            if remaining_amount in cache:
                return cache[remaining_amount]

            total_coins = 1 + min(pickCoin(remaining_amount - c) for c in coins)
            cache[remaining_amount] = total_coins
            return total_coins

        result = pickCoin(amount)
        return result if result < float('inf') else -1