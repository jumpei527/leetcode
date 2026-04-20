package main

// n = number of nodes in the tree
// Time:  O(n)
// Space: O(n)
func preorderTraversal(root *TreeNode) []int {
	result := []int{}
	var preorder func(*TreeNode)

	preorder = func(root *TreeNode) {
		if root == nil {
			return
		}

		result = append(result, root.Val)
		preorder(root.Left)
		preorder(root.Right)
	}

	preorder(root)

	return result
}
