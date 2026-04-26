package main

// n = number of nodes in the tree
// Time:  O(n)
// Space: O(1)
func flatten(root *TreeNode) {
	cur := root

	for cur != nil {
		if cur.Left != nil {
			prev := cur.Left
			for prev.Right != nil {
				prev = prev.Right
			}
			prev.Right = cur.Right
			cur.Right = cur.Left
			cur.Left = nil
		}
		cur = cur.Right
	}
}
