from main import FormattedTable

# different column sizes
table = FormattedTable()
table.add_column('col1')
table.add_columns(['col2','col3','col4'])
table.add_element('col1','aaaaa')
table.add_element('col2','bbb')
table.add_element('col3','cc')
table.add_element('col4','d')
table.add_element('col5','eeeeeeeeeee')
table.add_elements({'col1':['aa','aaa','aaaaaaa'], 'col2':['bbbbb','b'], 'col4':['ddd','dd','ddddd','dd','dddd'], 'col5':['ee']})
table.get_table()
print(table.save_to_file(file_name = "formatted_table.txt"))

# equal column sizes
table = FormattedTable(equal_column_size=True)
table.add_column('col1')
table.add_columns(['col2','col3','col4'])
table.add_element('col1','aaaaa')
table.add_element('col2','bbb')
table.add_element('col3','cc')
table.add_element('col4','d')
table.add_element('col5','eeeeeeeeeee')
table.add_elements({'col1':['aa','aaa','aaaaaaa'], 'col2':['bbbbb','b'], 'col4':['ddd','dd','ddddd','dd','dddd'], 'col5':['ee']})
table.get_table()
print(table.save_to_file(file_name = "formatted_table.txt", overwrite=False))