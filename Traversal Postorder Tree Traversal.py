# Python program or postorder traversal

''' A binary tree node has data, pointer to left child
and a pointer to right child '''
class newNode:

	# Constructor to create a newNode
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

''' Helper function that allocates a new node with the
given data and NULL left and right pointers. '''
def postorder(head):
	
	temp = head
	visited = set()
	while (temp and temp not in visited):
		
		# Visited left subtree
		if (temp.left and temp.left not in visited):
			temp = temp.left
			
		# Visited right subtree
		elif (temp.right and temp.right not in visited):
			temp = temp.right
		
		# Print node
		else:
			print(temp.data, end = " ")
			visited.add(temp)
			temp = head

''' Driver program to test above functions'''
if __name__ == '__main__':
	
	root = newNode(1)
	root.left = newNode(2)
	root.right = newNode(3)
	root.left.left = newNode(4)
	root.left.right = newNode(5)
	root.right.left = newNode(6)
	root.right.right = newNode(7)
	root.right.right.left = newNode(8)
	root.right.right.right = newNode(9)
	postorder(root)

# This code is contributed by
# SHUBHAMSINGH10
