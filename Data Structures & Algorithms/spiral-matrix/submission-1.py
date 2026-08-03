class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top = 0
        bottom = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1

        res = []
        while top <= bottom and left <= right:
            # Top row
            for col in range(left, right+1):
                res.append(matrix[top][col])
            top += 1

            # Right col
            for row in range(top, bottom+1):
                res.append(matrix[row][right])
            right -= 1

            # Bottom row (rev)
            if top <= bottom:
                print(right, left)
                for col in range(right, left-1, -1):
                    res.append(matrix[bottom][col])
            bottom -= 1


            # Left col (rev)
            if left <= right:
                for row in range(bottom, top-1, -1):
                    res.append(matrix[row][left])
            left += 1

        return res


# func spiralOrder(matrix [][]int) []int {
#     top, bot, left, right := 0, len(matrix)-1, 0, len(matrix[0])-1

#     var res []int

#     for left <= right && top <= bot {
#         // Get top row, until right bound
#         for i := left; i <= right; i++ {
#             res = append(res, matrix[top][i])
#         }
#         top++

#         // Get right row until bottom
#         for i := top; i <= bot; i++ {
#             res = append(res, matrix[i][right])
#         }
#         right--

#         // Get bottom row
#         if top <= bot {
#             for i := right; i >= left; i-- {
#                 res = append(res, matrix[bot][i])
#             }
#         }
#         bot--

#         // Get left column
#         if left <= right {
#             for i := bot; i >= top; i-- {
#                 res = append(res, matrix[i][left])
#             }
#         }
#         left++
#     }

#     return res
# }

# //   0 1 2
# // 0 1 2 3
# // 1 4 5 6
# // 2 7 8 9

# // 00 01 02 12 22 10 11
        