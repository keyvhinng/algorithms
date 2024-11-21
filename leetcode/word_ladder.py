from collections import deque

class Solution:

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        wordSet = set(wordList)

        queue = deque([(beginWord, 1)])
        visited = {beginWord}

        while queue:
            word, length = queue.popleft()

            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    next_word = word[:i] + c + word[i+1:]

                    if next_word == endWord:
                        return length+1

                    if next_word in wordSet and next_word not in visited:
                        visited.add(next_word)
                        queue.append((next_word, length+1))
        return 0
