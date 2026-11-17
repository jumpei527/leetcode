use std::collections::HashMap;

// n = s.len()
// Time: O(n)
// Space: O(n)
impl Solution {
    pub fn is_isomorphic(s: String, t: String) -> bool {
        let s: Vec<char> = s.chars().collect();
        let t: Vec<char> = t.chars().collect();

        let mut s_to_t = HashMap::new();
        let mut t_to_s = HashMap::new();

        for i in 0..s.len() {
            let a = s[i];
            let b = t[i];

            if let Some(&mapped) = s_to_t.get(&a) {
                if mapped != b {
                    return false;
                }
            } else {
                s_to_t.insert(a, b);
            }

            if let Some(&mapped) = t_to_s.get(&b) {
                if mapped != a {
                    return false;
                }
            } else {
                t_to_s.insert(b, a);
            }
        }

        true
    }
}
