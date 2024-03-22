import homemadetree as hmt
import homemadequeue as hmq

def bfs(tree: hmt.Tree) -> list: 
    root = tree.root()
    queue = hmq.Queue()
    queue.addtoQueue(root)
    i = 0
    array = []
    while (queue.emptyQueue() == False):
        x = queue.front()
        queue.removefromQueue()
        array.append(x)
        for i in range(0, len(array)):
            if array[i].left() is not None:
                queue.addtoQueue(array[i].left())
            if array[i].right() is not None:
                queue.addtoQueue(array[i].right)
    return array

def main():
    t = hmt.Tree()
    print(bfs(t))

if __name__ == "__main__":
    main()