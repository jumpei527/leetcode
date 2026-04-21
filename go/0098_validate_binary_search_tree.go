package main

import "math"

// n = number of nodes in the tree
// Time:  O(n)
// Space: O(n)
func isValidBST(root *TreeNode) bool {
	return dfsValidate(root, math.MinInt, math.MaxInt)
}

func dfsValidate(root *TreeNode, low int, high int) bool {
	if root == nil {
		return true
	}

	if low < root.Val && root.Val < high {
		return dfsValidate(root.Left, low, root.Val) && dfsValidate(root.Right, root.Val, high)
	} else {
		return false
	}
}
