package main

// n = number of nodes in the tree
// Time:  O(n)
// Space: O(n)
func isBalanced(root *TreeNode) bool {
	var checkBalance func(*TreeNode) (int, bool)

	checkBalance = func(root *TreeNode) (int, bool) {
		if root == nil {
			return 0, true
		}

		leftHeight, leftOk := checkBalance(root.Left)
		rightHeight, rightOk := checkBalance(root.Right)
		if !leftOk || !rightOk {
			return 0, false
		}

		if leftHeight-rightHeight > 1 || rightHeight-leftHeight > 1 {
			return 0, false
		}

		return max(leftHeight, rightHeight) + 1, true
	}

	_, balanced := checkBalance(root)
	return balanced

}
