use std::collections::HashMap;

// n = strs.len()
// m = max(strs[i].len())
// Time: O(n * mlogm)
// Space: O(n * m)
impl Solution {
    pub fn group_anagrams(strs: Vec<String>) -> Vec<Vec<String>> {
        let mut groups: HashMap<Vec<u8>, Vec<String>> = HashMap::new();

        for s in strs {
            let mut key = s.as_bytes().to_vec();
            key.sort_unstable();

            groups.entry(key).or_default().push(s);
        }

        groups.into_values().collect()
    }
}
