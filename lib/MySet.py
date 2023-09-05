class MySet:

    def __init__(self, enumerable=[]):
        # Initializing a dictionary to hold set elements
        self.dictionary = {}
        for value in enumerable:
            self.dictionary[value] = True

    def has(self, value):
        """ Checks if the value is present in the set """
        return value in self.dictionary

    def add(self, value):
        """ Adds the value to the set """
        self.dictionary[value] = True
        return self

    def delete(self, value):
        """ Removes the value from the set """
        self.dictionary.pop(value, None)
        return self

    def size(self):
        """ Returns the number of elements in the set """
        return len(self.dictionary)

    def clear(self):
        """ Removes all elements from the set """
        self.dictionary.clear()
        return self

    def __str__(self):
        """ Returns a string representation of the set """
        set_list = [str(key) for key in self.dictionary.keys()]
        return f'MySet: {{{", ".join(set_list)}}}'
