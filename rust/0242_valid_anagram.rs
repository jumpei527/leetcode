use std::collections::HashMap;

// n = max(s.len(), t.len())
// Time: O(n)
// Space: O(n)
impl Solution {
    pub fn is_anagram(s: String, t: String) -> bool {
        let mut s_map = HashMap::new();
        let mut t_map = HashMap::new();

        for c in s.chars() {
            *s_map.entry(c).or_insert(0) += 1;
        }

        for c in t.chars() {
            *t_map.entry(c).or_insert(0) += 1;
        }

        s_map == t_map
    }
}

// n = max(s.len(), t.len())
// Time: O(n log n)
// Space: O(n)
impl Solution2 {
    pub fn is_anagram(s: String, t: String) -> bool {
        let mut s: Vec<char> = s.chars().collect();
        let mut t: Vec<char> = t.chars().collect();

        s.sort_unstable();
        t.sort_unstable();

        s == t
    }
}
