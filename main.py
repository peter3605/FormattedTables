class FormattedTable:
    """
    Constructor for this class
        Params: equal_column_size: optional param that if set to True, makes all of the columns in the table be of
                                   the same width - default is False
    """
    def __init__(self, equal_column_size=False):
        self.columns = []
        self.elements = {}
        self.col_num = 0
        self.equal_column_size = equal_column_size

    """
    Add a singular column
        Params: col -> name of the column

    Ex: table.add_column('new column')
    """
    def add_column(self, col):
        col = str(col)
        self.columns.append(col)
        self.elements[col] = []
        self.col_num = self.col_num + 1

    """
    Add multiple columns
        Params: cols -> list of column names

    Ex: table.add_columns(['col1', 'col2', 'col3'])
    """
    def add_columns(self, cols):
        for col in cols:
            self.add_column(col)

    """
    Add a new table element
        Params: col -> name of the column that the element is in
                elem -> the element that is being inserted

    Ex: table.add_element('col1', 'newelem')
    """
    def add_element(self, col, elem):
        col = str(col)
        if col not in self.columns:
            self.add_columns([col])
        self.elements[col].append(str(elem))

    """
    Add multiple new table elements
        Params: elems -> a dictionary where the keys are the column names and the values is an array of elements being inserted
                         into that column

    Ex: table.add_elements({ 'col1':['elem1', 'elem2', 'elem3'], 'col2':['elem1','elem2'] })
    """
    def add_elements(self, elems):
        for col in elems.keys():
            for elem in elems[col]:
                self.add_element(col, elem)

    """
    Returns the width of the table
    """
    def __get_table_width(self):
        size = 1 + self.col_num
        if self.equal_column_size:
            size = size + (self.__get_longest_word("") + 2) * self.col_num
        else:
            # get the longest word for each column and added its length to the size
            for col in self.columns:
                longest = len(col)
                for elem in self.elements[col]:
                    longest = max(longest, len(elem))
                size = size + longest + 2
        return size

    """
    Returns the height of the table
    """
    def __get_table_height(self):
        size = 0
        for col in self.columns:
            size = max(size, len(self.elements[col]))
        return size
    
    """
    Returns the longest word in the specified column - could be the column name itself
        Params: col -> name of the column that you are looking for
    """
    def __get_longest_word(self, col):
        size = 0
        if self.equal_column_size:
            for col in self.columns:
                size = max(size, len(col))
                for elem in self.elements[col]:
                    size = max(size, len(elem))
        else:
            size = len(col)
            for elem in self.elements[col]:
                size = max(size, len(elem))
        return size

    """
    Returns a string containing the formatted table. Prints the output if the
    print_result param is specified as True
    """
    def get_table(self, print_result=False):
        table_width = self.__get_table_width()

        # start off with the top of the table
        output = '-' * table_width + '\n'

        # add the column names
        for col in self.columns:
            #get the longest word in the column
            longest = self.__get_longest_word(col)

            # figure out the left and right spacing between the vertical lines
            diff = longest - len(col)
            left = int(diff/2) + 1
            right = int(diff/2) + 1
            if diff % 2 != 0:
                right = right + 1

            # add the column name and spacing
            output += '|' + ' ' * left + col + " " * right

        # add the ending vertical line 
        output += '|\n' + '-' * table_width + '\n'

        # this keeps track of which elements we have added
        indexes = [0] * self.col_num

        # add the rows
        for _ in range(0, self.__get_table_height()):

            # for each row
            for i in range(0, self.col_num):
                col = self.columns[i]
                index = indexes[i]
                longest = self.__get_longest_word(col)

                # if there is another element to be added
                if index < len(self.elements[col]) and self.elements[col][index] is not None:

                    # figure out left and right spacing
                    diff = longest - len(self.elements[col][index])
                    left = int(diff/2) + 1
                    right = int(diff/2) + 1 
                    if diff % 2 != 0:
                        right = right + 1
                    
                    # add the element and spacing
                    output += '|' + ' ' * left + self.elements[col][index] + ' ' * right
                else:
                    # if there is no element to be added, add a dashed line
                    output += '| ' + '-' * longest + ' '

                #increment the index
                indexes[i] = indexes[i] + 1

            # add the bottom row
            output += '|\n' + '-' * table_width + '\n'

        #if print_result is true, print the table
        if print_result:
            print(output)
        return output

    """
    Saves the current table to a file
        Params: file_name -> the name of the file you want to save the table to - default is 'pretty_table.txt' in the same directory
                overwrite -> if False then it appends the table to the file - default is True
     Works best on .txt files
    """
    def save_to_file(self, file_name='formatted_table.txt', overwrite=True):
        #open file - mode should be append if overwrite is false
        if overwrite:
            f = open(file_name, 'w+')
        else:
            f = open(file_name, 'a')
            f.write('\n')

        #write to it
        f.write(self.get_table())

        #close
        f.close()

        #return file name
        return file_name
