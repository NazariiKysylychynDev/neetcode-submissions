class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def _check_duplication(set_, check):
            if check in set_:
                return True
            set_.add(check)

        box_checker = [[set(), set(), set()] for i in range(3)]
        col_duplication = [set() for i in range(9)]
        for row in range(len(board)):
            row_validation = set()
            for col in range(len(board)):
                element = board[row][col]
                if element == '.':
                    continue
                if _check_duplication(row_validation, element):
                    return False
                if _check_duplication(col_duplication[col], element):
                    return False
                if _check_duplication(box_checker[row // 3][col // 3], element):
                    return False
        return True