package main

// n = len(s)
// Time:  O(n)
// Space: O(n)
func isValid(s string) bool {
	brackets_pair := map[rune]rune{
		'}': '{',
		')': '(',
		']': '[',
	}
	stack := []rune{}

	for _, char := range s {
		if bracket, found := brackets_pair[char]; found {
			if len(stack) > 0 && stack[len(stack)-1] == bracket {
				stack = stack[:len(stack)-1]
			} else {
				return false
			}
		} else {
			stack = append(stack, char)
		}
	}

	return len(stack) == 0
}
