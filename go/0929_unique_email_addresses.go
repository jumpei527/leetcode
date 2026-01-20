package main

import "strings"

// n = len(emails)
// m = average length of an email
// Time:  O(n * m)
// Space: O(n * m)
func numUniqueEmails(emails []string) int {
	seen := make(map[string]struct{})

	for _, email := range emails {
		at := strings.Index(email, "@")
		local := email[:at]
		domain := email[at:]

		if plus := strings.Index(local, "+"); plus != -1 {
			local = local[:plus]
		}

		local = strings.ReplaceAll(local, ".", "")
		seen[local+domain] = struct{}{}
	}

	return len(seen)
}
