def adj_checker(grid, row, col, adj, block, block_id, len_blocks):
    ab = set(range(1, len_blocks+1))
    inverted_adj = [x for x in ab if x not in adj]
    inverted_adj = [x for x in inverted_adj if x <= block_id]
    print(inverted_adj)

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for i in range(len(block)):
        for j in range(len(block[0])):
            if block[i][j] == 1:
                for rd, cd in directions:
                    print(row + i + rd, col + j + cd)
                    if 0 <= row + i + rd < len(grid) and 0 <= col + j + cd < len(grid[0]) and grid[row + i + rd][col + j + cd] in adj and grid[row + i + rd][col + j + cd] not in inverted_adj:
                        return False
                    
    return True

adj = [2,1]

block = [[1, 1, 1], [0, 1, 0]]

grid = [[0,0,0], [4,0,2], [4,4,1]]
print(adj_checker(grid, 0,0,adj,block,3, 4))
