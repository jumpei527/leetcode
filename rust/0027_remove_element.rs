impl Solution {
    pub fn remove_element(nums: &mut Vec<i32>, val: i32) -> i32 {
        if (nums.is_empty()) {
            return 0;
        }

        let mut element_num = 0;
        for i in 0..nums.len() {
            if (nums[i] != val) {
                nums[element_num] = nums[i];
                element_num += 1;
            }
        }
        element_num as i32
    }
}
