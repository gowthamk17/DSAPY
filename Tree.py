class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None
    
    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level
    
    def print_tree(self, level=None):
        if level is None:
            level = self.get_level()
        space = ' ' * self.get_level() * 3
        prefix = space + "||==>" if self.parent else ""
        print(prefix + self.data)
        if level:
            for child in self.children:
                child.print_tree(level-1)

def build_tree():
    root = TreeNode('root')
    child1 = TreeNode('child1')
    child1.add_child(TreeNode('subchild1'))
    child1.add_child(TreeNode('subchild2'))
    child1.add_child(TreeNode('subchild3'))
    child2 = TreeNode('child2')
    child2.add_child(TreeNode('subchild1'))
    child2.add_child(TreeNode('subchild2'))
    child2.add_child(TreeNode('subchild3'))
    child3 = TreeNode('child3')
    child3.add_child(TreeNode('subchild1'))
    child3.add_child(TreeNode('subchild2'))
    child3.add_child(TreeNode('subchild3'))

    root.add_child(child1)
    root.add_child(child2)
    root.add_child(child3)

    root.print_tree(3)


if __name__ == '__main__':
    build_tree()