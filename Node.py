#Node.py

#  https://www.delftstack.com/de/howto/python/trees-in-python/




class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key
        self.parent = None
 
counter = 0 
list_node = []
def preorder(node):
    global counter
    #counter += 1
    print("counter" , counter)
    counter += 1
    #print("node key" , node.key)
    print("node " , node)
    #stringNode = str(node)
    #print("stringNode" ,stringNode)
    #print(stringNode)
    
    if node:
        print("node key" , node.key)
        list_node.append(node.key)
        print(list_node)
        preorder(node.left)   # er ist von hier recrusiv gegangen
                              # 1 root.left 
                              # 2 rufft root.left.left
                              # 3 rufft root.left.left.left None   example root.left.left.left = Node(90)
                              # 4 rufft root.left.left.right None  example root.left.left.right = Node(100)
        preorder(node.right)  # 5 rufft root.left.right node key 50
                              # 6 rufft root.left.right.left None   example root.left.right.left = Node(300)
                              # 7 rufft root.left.right.right None  example root.left.right.right = Node(400)
                              # 8 root.right node key 89
        return "hallo from preorder"
    return "hello weil gehe ich raus"
        
root = Node(10)

root.left = Node(34)
root.right = Node(89)
root.left.left = Node(45)
root.left.right = Node(50)
#root.left.left.left = Node(90)
#root.left.left.right = Node(100)
#root.left.left.right.left = Node(200)
#root.left.right.left = Node(300)
#root.left.right.right = Node(400)

#print(type(root.left.key))
#print(type(root.right.key))
#print(type(root.left.left.key))
#print(type(root.left.right.key))


#print(root.left.key)
#print(root.right.key)
#print(root.left.left.key)
#print(root.left.right.key)

print(preorder(root))
