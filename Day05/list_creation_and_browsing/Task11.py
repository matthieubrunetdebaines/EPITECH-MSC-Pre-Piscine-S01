my_first_list = [4 , 5 , 6]
my_second_list = [1 , 2 , 3]
my_first_list . extends ( my_second_list )

# We add my_second_list elements to the end of my_first_list

my_first_list = [7 , 8 , 9]
my_second_list = [4 , 5 , 6]
my_first_list = [* my_first_list , * my_second_list ]

# same same but different