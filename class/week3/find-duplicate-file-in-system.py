class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        dup_files = {}
        dup_file_paths = []

        for i in range(len(paths)):
            dir_path = ""
            file_ = ""
            content  = ""
            spaces_id = [0, 0]
            j, l = 0, 0
            while j < len(paths[i]):
                if paths[i][j] == " ":
                    if spaces_id[0] == 0:
                        dir_path += paths[i][:j]
                    spaces_id[0] = spaces_id[0] + 1
                    spaces_id[1] = j
                elif paths[i][j] == "(":
                    file_ += dir_path + "/" + paths[i][spaces_id[1] + 1:j]
                    l = j
                elif paths[i][j] == ")":
                    content = paths[i][l + 1:j]
                    if content not in dup_files:
                        dup_files[content] = [file_]
                    else:
                        dup_files[content].append(file_)

                    file_ = ""
                
                j += 1
        for value in dup_files.values():
            if len(value) > 1:
                dup_file_paths.append(value)

        return dup_file_paths
                
