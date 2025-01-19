# n = len(path)
# Time: O(n)
# Space: O(n)


class Solution:
    def simplifyPath(self, path: str) -> str:
        directories = path.split("/")
        path = []

        for dir in directories:
            if dir == "." or dir == "":
                continue
            elif dir == "..":
                if path:
                    path.pop()
            else:
                path.append(dir)

        return "/" + "/".join(path)
