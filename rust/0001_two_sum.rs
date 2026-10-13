use std::collections::HashMap;

impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let mut num_map = HashMap::new();

        for (idx, &num) in nums.iter().enumerate() {
            let complement = target - num;
            if let Some(&prev_idx) = num_map.get(&complement) {
                return vec![prev_idx as i32, idx as i32];
            }
            num_map.insert(num, idx);
        }

        vec![]
    }
}
