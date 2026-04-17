package main

// Definition for a binary tree node.
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

// n = number of nodes in the tree
// Time:  O(n)
// Space: O(n)
func postorderTraversal(root *TreeNode) []int {
	result := []int{}
	var postorder func(*TreeNode)

	postorder = func(root *TreeNode) {
		if root == nil {
			return
		}

		postorder(root.Left)
		postorder(root.Right)
		result = append(result, root.Val)
	}

	postorder(root)

	return result
}
