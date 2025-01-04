class Solution:
    def countPalindromicSubsequence(self, s:str) -> int:
        positions = {}
        for idx, char in enumerate(s):
            pos_by_char = positions.get(char, [])
            pos_by_char.append(idx)
            positions[char] = pos_by_char;

        ans = 0

        unique_letters = set(list(s))

        for char in unique_letters:
            pos_by_char = positions[char]

            left = pos_by_char[0]
            right = pos_by_char[-1]

            between = set()

            for i in range(left+1, right):
                between.add(s[i])

            ans += len(between)

        return ans

