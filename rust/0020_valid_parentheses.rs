impl Solution {
    pub fn is_valid(s: String) -> bool {
        let mut stack = Vec::new();

        for c in s.chars() {
            let expected = match c {
                '(' | '{' | '[' => {
                    stack.push(c);
                    continue;
                }
                ')' => '(',
                '}' => '{',
                ']' => '[',
                _ => return false,
            };

            if stack.pop() != Some(expected) {
                return false;
            }
        }

        stack.is_empty()
    }
}
