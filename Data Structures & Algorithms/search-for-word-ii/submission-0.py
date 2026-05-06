class TrieNode:
    def __init__(self):
        self.children = {}
        self.wordEnd = False

    def addWord(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.wordEnd = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for word in words:
            root.addWord(word)

        ROWS, COLS = len(board), len(board[0])
        res, vis = set(), set()
        def dfs(r, c, node, word):
            if (r < 0 or c < 0 or
            r >= ROWS or c >= COLS or
            (r, c) in vis or board[r][c] not in node.children):
                return
            
            vis.add((r, c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.wordEnd:
                res.add(word)

            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)
            vis.remove((r, c))

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")

        return list(res)