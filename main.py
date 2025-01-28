import matplotlib.pyplot as plt
import numpy as np

def display_grid(grid):
    fig, ax = plt.subplots()
    ax.set_xticks(range(len(grid[0]) + 1))
    ax.set_yticks(range(len(grid) + 1))
    ax.grid(True)

    colors = plt.cm.get_cmap('tab20', max(max(row) for row in grid) + 1)

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] != 0:
                ax.add_patch(plt.Rectangle((j, len(grid) - i - 1), 1, 1, color=colors(grid[i][j])))

    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()

def can_place(grid, block, row, col):
    for i in range(len(block)):
        for j in range(len(block[i])):
            if block[i][j] == 1:
                if row + i >= len(grid) or col + j >= len(grid[0]) or grid[row + i][col + j] != 0:
                    return False
    return True

def place(grid, block, row, col, block_id):
    for i in range(len(block)):
        for j in range(len(block[i])):
            if block[i][j] == 1:
                grid[row + i][col + j] = block_id

def remove(grid, block, row, col):
    for i in range(len(block)):
        for j in range(len(block[i])):
            if block[i][j] == 1:
                grid[row + i][col + j] = 0

def get_rots(block):
    rotations = [block]
    for _ in range(3):  
        block = [list(row) for row in zip(*block[::-1])]
        rotations.append(block)
    return rotations

def adj_checker(grid, row, col, adj, block, block_id, len_blocks):
    ab = set(range(1, len_blocks+1))
    inverted_adj = [x for x in ab if x not in adj]
    inverted_adj = [x for x in inverted_adj if x <= block_id]

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for i in range(len(block)):
        for j in range(len(block[0])):
            if block[i][j] == 1:
                for rd, cd in directions:
                    if 0 <= row + i + rd < len(grid) and 0 <= col + j + cd < len(grid[0]) and grid[row + i + rd][col + j + cd] in adj and grid[row + i + rd][col + j + cd] not in inverted_adj:
                        return False
                    
    return True

'''def final_adj_checker(grid, adj):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] != 0:
                block_id = grid[row][col]
                for rd, cd in directions:
                    if 0 <= row + rd < len(grid) and 0 <= col + cd < len(grid[0]) and grid[row + rd][col + cd] != 0 and grid[row + rd][col + cd] in adj[block_id]:
                        return False
    return True'''
                
                
def solve(grid, blocks, adj, block_index=0):
    if block_index == len(blocks):
        '''print(grid)
        inverted_adj = {}
        bl = set(range(1, len(blocks)+1))
        for key in adj:
            inverted_adj[key] = list(bl-set(adj[key]))
        i=0
        for x in blocks:
            i += 1
            if sum(sum(r) for r in x) > 1:
                inverted_adj[i].append(i)
        if final_adj_checker(grid, inverted_adj):
            return True  # All blocks placed
        print("failed final check")'''
        return True

    block_id = block_index + 1
    block = blocks[block_index]

    for rot in get_rots(block):
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if can_place(grid, rot, row, col):
                    if block_id in adj:
                        req_blocks = adj[block_id]
                        if not adj_checker(grid, row, col, req_blocks, rot, block_id, len(blocks)):
                            continue
                    place(grid, rot, row, col, block_id)
                    if solve(grid, blocks, adj, block_index + 1):
                        return True
                    remove(grid, rot, row, col)
    return False                        
    
def main():
    row = int(input("Enter the number of rows for the grid: "))
    col = int(input("Enter the number of columns for the grid: "))
    grid = [[0 for a in range(col)] for a in range(row)]

    blocks = []
    nb = int(input("Enter the number of blocks: "))
    print("\n block input must be in the form of the smallest rectangle containing the block - so a T shaped block would be [[1 1 1], [0 1 0]].\n add 1s where the block exists, and 0 where it doesnt.\n")
    for b in range(nb):
        print(f"\nEnter block {b + 1}:")
        block_rows = int(input("  Number of rows: "))
        block = []
        for r in range(block_rows):
            row_input = input(f"  Enter row {r + 1} (e.g., 1 1 0): ")
            row = [int(x) for x in row_input.split()]
            block.append(row)
        blocks.append(block)

    adj = {}
    num_pairs = int(input("\nEnter the number of adjacent pair conditions: "))
    for a in range(num_pairs):
        pair = input("Enter a pair (e.g., 1 2): ")
        block1, block2 = map(int, pair.split())
        if block1 not in adj:
            adj[block1] = []
        if block2 not in adj:
            adj[block2] = []
        adj[block1].append(block2)
        adj[block2].append(block1)

    bl = set(range(1, nb+1))
    for key in adj:
        adj[key] = list(bl-set(adj[key]))
    
    if solve(grid, blocks, adj):
        print("\nSolution found!")
        print(grid)
        display_grid(grid)
    else:
        print("\n failed")

main()