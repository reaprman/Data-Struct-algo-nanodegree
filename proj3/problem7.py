# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode()

    def insert(self, path_parts, handler):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        current_node = self.root

        for part in path_parts:
            if part not in current_node.children:
                current_node.insert(part)
            current_node = current_node.children[part]
            current_node.path_part = part
        current_node.handler = handler
        pass


    def find(self, path_parts):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        current_node = self.root

        for part in path_parts:
            if part in current_node.children.keys():
                current_node = current_node.children[part]
            else:
                return None
        
        return current_node.handler


# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self):
        # Initialize the node with children as before, plus a handler
        self.children = dict()
        self.handler = None
        self.path_part = ""

    def insert(self, path_part):
        # Insert the node as before
        self.children[path_part] = RouteTrieNode()


# The Router class will wrap the Trie and handle 
class Router:
    def __init__(self, root_handler):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.router_Trie = RouteTrie()
        self.router_Trie.root.handler = root_handler

    def add_handler(self, path, handler):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie

        trie = self.router_Trie
        trie.insert(self.split_path(path), handler)


    def lookup(self, path):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        trie = self.router_Trie
        if path == "/":
            return trie.root.handler

        search_result = trie.find(self.split_path(path))
        if search_result != None:
            return search_result
        else:
            return "not found handler"
        


    def split_path(self, path):
        # you need to split the path into parts for 
        # both the add_handler and loopup functions,
        # so it should be placed in a function here
        path_parts = path.split("/")
        if path_parts[len(path_parts)-1] == '':
            path_parts = path_parts[:len(path_parts)-1]
        return path_parts

        # Here are some test cases and expected outputs you can use to test your implementation

# create the router and add a route
router = Router("root handler") # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output
print(router.lookup("/")) # should print 'root handler'
print(router.lookup("/home")) # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about")) # should print 'about handler'
print(router.lookup("/home/about/")) # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/me")) # should print 'not found handler' or None if you did not implement one