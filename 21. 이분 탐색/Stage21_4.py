import sys

if __name__ == '__main__':
    N,M = map(int,sys.stdin.readline().rstrip().split())
    tree_list = list(map(int,sys.stdin.readline().rstrip().split()))

    min_tree = 0; max_tree = max(tree_list);

    while min_tree <= max_tree:
        mid_tree = (min_tree+max_tree)//2
        total_cut_tree = 0
        for tree in tree_list:
            if mid_tree < tree:
                total_cut_tree += tree - mid_tree

        if total_cut_tree >= M:
            min_tree = mid_tree + 1
        else:
            max_tree = mid_tree - 1

    print(max_tree)
