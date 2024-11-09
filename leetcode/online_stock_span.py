class StockSpanner:

    def __init__(self):
        self.num_stack = []
        self.idx_stack = []
        self.count = 0

    def next(self, price: int) -> int:
        ans = 1
        in_loop = False

        while len(self.num_stack) and price >= self.num_stack[-1]:
            in_loop = True
            self.num_stack.pop()
            removed = self.idx_stack.pop()

        self.num_stack.append(price)

        if in_loop:
            self.idx_stack.append(removed)
            ans = self.count - self.idx_stack[-1] + 1
        else:
            self.idx_stack.append(self.count)

        self.count += 1

        return ans

sp = StockSpanner()
sp.next(100)
sp.next(80)
sp.next(60)
sp.next(70)
sp.next(60)
sp.next(75)
sp.next(85)

