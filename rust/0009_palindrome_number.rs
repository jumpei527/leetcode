// Time: O(n)
// Space: O(n)
impl Solution {
    pub fn is_palindrome(x: i32) -> bool {
        let s = x.to_string();
        let reversed : String = s.chars().rev().collect();

        s == reversed
    }
}


// Time: O(log(n))
// Space: O(1)
impl Solution2 {
    pub fn is_palindrome(x: i32) -> bool {
        if x < 0 {
            return false;
        }

        let mut n = x as i64;
        let mut reversed = 0_i64;

        while n > 0 {
            let digit = n % 10;
            reversed = reversed * 10 + digit;
            n /= 10;
        }

        x as i64 == reversed
    }
}
