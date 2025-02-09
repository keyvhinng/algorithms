class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        n = len(s)
        if n%2:
            return False

        locked_open = []
        unlocked = []

        for i in range(n):
            c = s[i]
            if locked[i] == '1':
                if c == '(':
                    locked_open.append(i)
                else:
                    if locked_open:
                        locked_open.pop()
                    elif unlocked:
                        unlocked.pop()
                    else:
                        return False
            else:
                unlocked.append(i)

        while locked_open and unlocked and locked_open[-1] < unlocked[-1]:
            locked_open.pop()
            unlocked.pop()

        if locked_open:
            return False

        return True
