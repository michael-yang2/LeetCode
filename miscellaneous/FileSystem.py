class Directory:
    def __init__(self):
        self.subdirectories = {}
        self.files = {}
class FileSystem:

    def __init__(self):
        self.root = Directory()
        self.root.subdirectories[''] = Directory()

    def ls(self, path: str) -> List[str]:
        dirs = path.split('/')
        if path == '/':
            dirs.pop()
        curr_dir = self.root
        for i in range(len(dirs)-1):
            d = dirs[i]
            if d in curr_dir.subdirectories:
                curr_dir = curr_dir.subdirectories[d]
        if dirs[-1] in curr_dir.files and len(dirs) > 1:
            return [dirs[-1]]
        else:
            curr_dir = curr_dir.subdirectories[dirs[-1]]
            to_return = list(curr_dir.subdirectories.keys())+list(curr_dir.files.keys())
            to_return.sort()
            return to_return

    def mkdir(self, path: str) -> None:
        dirs = path.split('/')
        curr_dir = self.root
        for d in dirs:
            if d not in curr_dir.subdirectories:
                curr_dir.subdirectories[d] = Directory()
            curr_dir = curr_dir.subdirectories[d]

    def addContentToFile(self, filePath: str, content: str) -> None:
        dirs = filePath.split('/')
        curr_dir = self.root
        for i in range(len(dirs)-1):
            d = dirs[i]
            if d in curr_dir.subdirectories:
                curr_dir = curr_dir.subdirectories[d]
        if dirs[-1] in curr_dir.files:
            curr_dir.files[dirs[-1]] = curr_dir.files[dirs[-1]]+content
        else:
            curr_dir.files[dirs[-1]] = content

    def readContentFromFile(self, filePath: str) -> str:
        dirs = filePath.split('/')
        curr_dir = self.root
        for i in range(len(dirs)-1):
            d = dirs[i]
            if d in curr_dir.subdirectories:
                curr_dir = curr_dir.subdirectories[d]
        if dirs[-1] in curr_dir.files:
            return curr_dir.files[dirs[-1]]


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)