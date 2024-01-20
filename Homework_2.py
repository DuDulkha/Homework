            ### Question 1:

my_list_str = ['California', 'Texas', 'Frorida', 'Ohio']
type(my_list_str)
my_list_num = [10.04, 7.43, 5.58, 3.16]
type(my_list_num)
my_list_str.extend(my_list_num)
print(my_list_str)

my_list_str[2]     # 3rd element
my_list_str[:1]    # 0th element
my_list_str[:2]    # 0 and 1st element
my_list_str[1:]    # 1 and up to last element
my_list_str[::-1]  # reverse list 
my_list_str[::-2]  # reverse list, but every second element starting from the last
my_list_str[-1]    # last element
my_list_str[-2]    # second to the last element

# join elements
my_list_str = ['California', 'Texas', 'Frorida', 'Ohio']
",".join(my_list_str)
" ".join(['California', 'Texas', 'Frorida'])
"".join(['California', 'Texas', 'Frorida']) 
"-".join(['California', 'Texas', 'Frorida'])

# append list
my_list_str.append('New York')

# insert into list
my_list_num.insert(4, 5.2)

# extend list
my_list_str.extend(my_list_num)

# remove by index
my_list_str.pop() 
my_list_str.pop(2) # second item
# or
del my_list_str[2]
del my_list_str[0:2]

# remove by value
my_list_str.remove(5.58)
my_list_str[0] = 7.0

            
            ### Question 2: ###
import datetime

# String to datetime
y = "2024-Dec-20"
mydate = datetime.datetime.strptime(y, "%Y-%b-%d")
print(mydate)

# Datetime to string
now = datetime.datetime.now()
t = now.strftime("%Y-%m-%d")
print("Today is:", t)


            ### Question 3: ###
x = ['California', 'Texas', 'Frorida', 'Ohio']
y = [10.04, 7.43, 5.58, 3.16]
states_pop_growth_dic = {"states":x, "pop_growth":y}
print(states_pop_growth_dic)

# Another way
my_dict = dict(zip(x, y))
print(my_dict)