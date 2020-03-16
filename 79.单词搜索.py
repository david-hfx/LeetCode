#
# @lc app=leetcode.cn id=79 lang=python3
#
# [79] 单词搜索
#
# https://leetcode-cn.com/problems/word-search/description/
#
# algorithms
# Medium (37.97%)
# Likes:    152
# Dislikes: 0
# Total Accepted:    12.8K
# Total Submissions: 33.7K
# Testcase Example:  '[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]\n"ABCCED"'
#
# 给定一个二维网格和一个单词，找出该单词是否存在于网格中。
#
# 单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。
#
# 示例:
#
# board =
# [
# ⁠ ['A','B','C','E'],
# ⁠ ['S','F','C','S'],
# ⁠ ['A','D','E','E']
# ]
#
# 给定 word = "ABCCED", 返回 true.
# 给定 word = "SEE", 返回 true.
# 给定 word = "ABCB", 返回 false.
#
#
#! backtracking, dfs
#! 回溯算法 + 深度优先搜索
class Solution:

    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board:
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(board, i, j, word):
                    return True
        return False

    # check whether can find word, start at (i,j) position
    def dfs(self, board, i, j, word):
        if len(word) == 0:  #! all the characters are checked
            return True
        if i < 0 or i >= len(board) or j < 0 or j >= len(
                board[0]) or word[0] != board[i][j]:
            return False
        tmp = board[i][
            j]  #! first character is found, check the remainning part
        board[i][j] = '#'  #! avoid visit again
        #! check whether can find 'word' along one direction
        res = self.dfs(board, i + 1, j, word[1:]) or self.dfs(
            board, i - 1, j,
            word[1:]) or self.dfs(board, i, j + 1, word[1:]) or self.dfs(
                board, i, j - 1, word[1:])
        board[i][j] = tmp  #! return the word for next search
        return res
