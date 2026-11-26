// n = nums.len()
// Time: O(log n)
// Space: O(1)
impl Solution {
    pub fn search_range(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let mut left = 0;
        let mut right = nums.len();

        while left < right {
            let mid = (left + right) / 2;

            if nums[mid] < target {
                left = mid + 1;
            } else {
                right = mid;
            }
        }

        let start = left;

        if start == nums.len() || nums[start] != target {
            return vec![-1, -1]
        }

        right = nums.len() - 1;

        while left < right {
            let mid = (left + right + 1) / 2;

            if nums[mid] > target {
                right = mid - 1;
            } else {
                left = mid;
            }
        }

        vec![start as i32, right as i32]
    }
}
