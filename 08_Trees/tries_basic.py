# ============================================================
# Tries Basics
# ============================================================
#
# A Trie is a tree used to store strings.
#
# It is also called a prefix tree.
#
# Prefix means the beginning part of a word.
#
# Example:
#
#   "car"
#   "cat"
#
# Both words start with:
#
#   "ca"
#
# A trie stores shared prefixes only once.
#
# ------------------------------------------------------------
# SIMPLE TRIE EXAMPLE
# ------------------------------------------------------------
#
# Store these words:
#
#   car
#   cat
#   dog
#
# Trie:
#
#              root
#             /    \
#            c      d
#            |      |
#            a      o
#           / \     |
#          r   t    g
#
# Words stored:
#
#   c -> a -> r = car
#   c -> a -> t = cat
#   d -> o -> g = dog
#
# Notice:
#
#   car and cat share c -> a.
#
# ------------------------------------------------------------
# WHY TRIES ARE USEFUL
# ------------------------------------------------------------
#
# Tries are useful for:
#
#   autocomplete
#   spell check
#   word search
#   prefix search
#   dictionary lookup
#
# Example:
#
#   Words:
#       car
#       cat
#       cart
#
#   Prefix:
#       ca
#
#   Matches:
#       car
#       cat
#       cart
#
# ------------------------------------------------------------
# TRIE VS BST
# ------------------------------------------------------------
#
# BST:
#
#   Stores whole values in each node.
#
# Example:
#
#              "cat"
#             /     \
#          "car"    "dog"
#
# Trie:
#
#   Stores one character at a time.
#
# Example:
#
#              root
#               |
#               c
#               |
#               a
#              / \
#             r   t
#
# ------------------------------------------------------------
# BIG O / SPEED
# ------------------------------------------------------------
#
# Trie insert:
#
#   O(k)
#
# Trie search:
#
#   O(k)
#
# Trie prefix search:
#
#   O(k)
#
# k = length of the word or prefix.
#
# Why?
#   We process one character at a time.
#
# Example:
#
#   Search for "cat"
#
#   c -> a -> t
#
#   That checks 3 characters.
#
# ------------------------------------------------------------
# SPACE COMPLEXITY
# ------------------------------------------------------------
#
# Trie storage:
#
#   O(total characters)
#
# Why?
#   Each node stores a character path.
#
# But shared prefixes save space.
#
# Example:
#
#   car
#   cat
#
# Without sharing:
#
#   car = 3 characters
#   cat = 3 characters
#   total = 6
#
# With trie sharing:
#
#   shared c
#   shared a
#   r
#   t
#
#   total nodes after root = 4
#
# ------------------------------------------------------------
# IMPORTANT NOTE
# ------------------------------------------------------------
#
# A trie needs a way to mark the end of a word.
#
# Example:
#
#   Words:
#
#       car
#       cart
#
# Trie path:
#
#       c -> a -> r -> t
#
# Problem:
#
#   If we only follow characters, how do we know "car" is also
#   a complete word?
#
# Fix:
#
#   Mark the node for r as end_of_word = True.
#
# That means:
#
#   c -> a -> r is a word.
#   c -> a -> r -> t is also a word.
# ============================================================


class TrieNode:
    def __init__(self):
        # Each node stores children in a dictionary.
        #
        # Key:
        #   character
        #
        # Value:
        #   another TrieNode
        #
        # Example:
        #
        #   children["c"] points to the node for c.
        self.children = {}

        # This tells us if this node completes a word.
        #
        # Example:
        #
        #   For the word "car":
        #
        #   c -> a -> r
        #
        #   The r node should have end_of_word = True.
        self.end_of_word = False


class Trie:
    def __init__(self):
        # The root does not store a letter.
        #
        # It is just the starting point.
        self.root = TrieNode()

    # --------------------------------------------------------
    # Insert word
    # --------------------------------------------------------
    #
    # Insert adds a word one character at a time.
    #
    # Example:
    #
    #   insert("cat")
    #
    # Steps:
    #
    #   start at root
    #   add/follow c
    #   add/follow a
    #   add/follow t
    #   mark t as end_of_word
    #
    # Time Complexity:
    #
    #   O(k)
    #
    # k = length of the word.
    # --------------------------------------------------------

    def insert(self, word):
        current = self.root

        for char in word:
            # If the character path does not exist, create it.
            if char not in current.children:
                current.children[char] = TrieNode()

            # Move to the next character node.
            current = current.children[char]

        # Mark the last character as the end of a word.
        current.end_of_word = True

    # --------------------------------------------------------
    # Search word
    # --------------------------------------------------------
    #
    # Search checks if a full word exists.
    #
    # Important:
    #
    #   The path must exist.
    #   The last node must be marked end_of_word.
    #
    # Example:
    #
    #   Words inserted:
    #
    #       car
    #       cart
    #
    #   search("car") returns True
    #   search("ca") returns False unless "ca" was inserted
    #
    # Time Complexity:
    #
    #   O(k)
    # --------------------------------------------------------

    def search(self, word):
        current = self.root

        for char in word:
            if char not in current.children:
                return False

            current = current.children[char]

        return current.end_of_word

    # --------------------------------------------------------
    # Starts with prefix
    # --------------------------------------------------------
    #
    # This checks if any word starts with a prefix.
    #
    # Example:
    #
    #   Words:
    #       car
    #       cat
    #       dog
    #
    #   starts_with("ca") returns True
    #   starts_with("do") returns True
    #   starts_with("z") returns False
    #
    # Time Complexity:
    #
    #   O(k)
    #
    # k = length of the prefix.
    # --------------------------------------------------------

    def starts_with(self, prefix):
        current = self.root

        for char in prefix:
            if char not in current.children:
                return False

            current = current.children[char]

        return True

    # --------------------------------------------------------
    # Insert with explanation
    # --------------------------------------------------------

    def insert_with_steps(self, word):
        print(f'Insert word: "{word}"')
        print("-" * 60)

        current = self.root

        print("Start at root.")

        for char in word:
            if char not in current.children:
                print(f'Character "{char}" does not exist yet.')
                print(f'Create node for "{char}".')
                current.children[char] = TrieNode()
            else:
                print(f'Character "{char}" already exists.')
                print(f'Follow existing path for "{char}".')

            current = current.children[char]
            print()

        current.end_of_word = True
        print(f'Mark the last node as end_of_word = True.')
        print(f'This means "{word}" is now stored.')
        print()

    # --------------------------------------------------------
    # Search with explanation
    # --------------------------------------------------------

    def search_with_steps(self, word):
        print(f'Search for word: "{word}"')
        print("-" * 60)

        current = self.root

        print("Start at root.")

        for char in word:
            print(f'Look for "{char}".')

            if char not in current.children:
                print(f'"{char}" was not found.')
                print(f'Result: "{word}" is not stored.')
                print()
                return False

            print(f'"{char}" was found. Move to that node.')
            current = current.children[char]
            print()

        print("Reached the last character.")
        print(f"end_of_word = {current.end_of_word}")

        if current.end_of_word:
            print(f'Result: "{word}" is a complete word.')
        else:
            print(f'Result: "{word}" is only a prefix, not a complete word.')

        print()
        return current.end_of_word

    # --------------------------------------------------------
    # Prefix search with explanation
    # --------------------------------------------------------

    def starts_with_steps(self, prefix):
        print(f'Prefix search: "{prefix}"')
        print("-" * 60)

        current = self.root

        print("Start at root.")

        for char in prefix:
            print(f'Look for "{char}".')

            if char not in current.children:
                print(f'"{char}" was not found.')
                print(f'Result: No stored word starts with "{prefix}".')
                print()
                return False

            print(f'"{char}" was found. Move to that node.')
            current = current.children[char]
            print()

        print(f'Result: At least one stored word starts with "{prefix}".')
        print()
        return True


# ------------------------------------------------------------
# Build a Trie
# ------------------------------------------------------------

trie = Trie()

print("Tries Basics")
print("=" * 60)
print()

print("A trie stores words one character at a time.")
print("Shared prefixes are stored only once.")
print()

print("Example words:")
print("car, cat, cart, dog")
print()

print("Visual idea:")
print()
print("              root")
print("             /    \\")
print("            c      d")
print("            |      |")
print("            a      o")
print("           / \\     |")
print("          r   t    g")
print("          |")
print("          t")
print()

print("Words:")
print("c -> a -> r       = car")
print("c -> a -> t       = cat")
print("c -> a -> r -> t  = cart")
print("d -> o -> g       = dog")
print()


# ------------------------------------------------------------
# Insert examples
# ------------------------------------------------------------

print("Insert Examples")
print("=" * 60)
print()

trie.insert_with_steps("car")
trie.insert_with_steps("cat")
trie.insert_with_steps("cart")
trie.insert_with_steps("dog")


# ------------------------------------------------------------
# Search examples
# ------------------------------------------------------------

print("Search Examples")
print("=" * 60)
print()

trie.search_with_steps("car")
trie.search_with_steps("cart")
trie.search_with_steps("ca")
trie.search_with_steps("dog")
trie.search_with_steps("cow")


# ------------------------------------------------------------
# Prefix examples
# ------------------------------------------------------------

print("Prefix Search Examples")
print("=" * 60)
print()

trie.starts_with_steps("ca")
trie.starts_with_steps("car")
trie.starts_with_steps("do")
trie.starts_with_steps("z")


# ------------------------------------------------------------
# Complexity summary
# ------------------------------------------------------------

print("Complexity Summary")
print("=" * 60)

print("Let k = length of the word or prefix.")
print()

print("Insert word:")
print("O(k)")
print("Why? We process one character at a time.")
print()

print("Search word:")
print("O(k)")
print("Why? We follow one character path at a time.")
print()

print("Prefix search:")
print("O(k)")
print("Why? We only check the prefix characters.")
print()

print("Space:")
print("O(total characters)")
print("But shared prefixes can save space.")
print()


