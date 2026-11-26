impl Solution {
    pub fn valid_path(n: i32, edges: Vec<Vec<i32>>, source: i32, destination: i32) -> bool {
        let mut graph = vec![vec![]; n as usize];

        for edge in edges {
            let a = edge[0] as usize;
            let b = edge[1] as usize;

            graph[a].push(b);
            graph[b].push(a);
        }

        let mut visited = vec![false; n as usize];
        let mut stack = vec![source as usize];

        visited[source as usize] = true;

        while let Some(node) = stack.pop() {
            if node == destination as usize {
                return true
            }

            for &next in &graph[node] {
                if !visited[next] {
                    visited[next] = true;
                    stack.push(next);
                }
            }
        }

        false
    }
}
