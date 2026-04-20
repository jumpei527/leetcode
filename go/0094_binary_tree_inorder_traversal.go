package main

// n = number of nodes in the tree
// Time:  O(n)
// Space: O(n)
func inorderTraversal(root *TreeNode) []int {
	result := []int{}

	var inorder func(*TreeNode)

	inorder = func(root *TreeNode) {
		if root == nil {
			return
		}

		inorder(root.Left)
		result = append(result, root.Val)
		inorder(root.Right)
	}

	inorder(root)

	return result
}
