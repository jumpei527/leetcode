// n = chars.len()
// Time: O(n)
// Space: O(1)
impl Solution {
    pub fn compress(chars: &mut Vec<char>) -> i32 {
        let mut read_idx: usize = 0;
        let mut write_idx: usize = 0;
        let n = chars.len();

        while read_idx < n {
            let c = chars[read_idx];
            let mut counter = 0;
            while read_idx < n && chars[read_idx] == c {
                read_idx += 1;
                counter += 1;
            }

            chars[write_idx] = c;
            write_idx += 1;

            if counter > 1 {
                for digit in counter.to_string().chars() {
                    chars[write_idx] = digit;
                    write_idx += 1;
                }
            }
        }

        write_idx as i32
    }
}
