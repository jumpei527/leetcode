package main

import "slices"

// n = number of nodes in the tree
// Time:  O(n)
// Space: O(n)
func pathSum(root *TreeNode, targetSum int) [][]int {
	results := [][]int{}

	var dfs func(*TreeNode, []int, int)

	dfs = func(node *TreeNode, curPath []int, curTarget int) {
		if node == nil {
			return
		}

		curPath = append(curPath, node.Val)
		curTarget -= node.Val
		if node.Left == nil && node.Right == nil {
			if curTarget == 0 {
				results = append(results, slices.Clone(curPath))
			}
		}

		dfs(node.Left, curPath, curTarget)
		dfs(node.Right, curPath, curTarget)
	}

	dfs(root, []int{}, targetSum)

	return results
}
