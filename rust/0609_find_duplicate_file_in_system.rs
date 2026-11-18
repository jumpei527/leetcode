use std::collections::HashMap;

// n = paths.len()
// m = paths[i].len()
// Time: O(n * m)
// Space: O(n * m)
impl Solution {
    pub fn find_duplicate(paths: Vec<String>) -> Vec<Vec<String>> {
        let mut groups: HashMap<String, Vec<String>> = HashMap::new();

        for path in paths {
            let mut parts = path.split_whitespace();
            let dir = parts.next().unwrap();

            for part in parts {
                let (name, content) = part.split_once('(').unwrap();
                let content = content.trim_end_matches(')');

                let full_path = format!("{}/{}", dir, name);

                groups.entry(content.to_string()).or_default().push(full_path);
            }
        }

        groups.into_values().filter(|group| group.len() > 1).collect()
    }
}
