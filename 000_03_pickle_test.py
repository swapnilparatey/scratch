import pickle

#some_list = ['flowers', 'animals', 'colors', 'ocean', 'earth']
some_list = { 'swapnil':[32,'male','india'], 'trevor':[31,'male','dripping'], 'julia':[31,'female','austin']}
output = pickle.dumps(some_list, protocol=pickle.HIGHEST_PROTOCOL)
back_to_list = pickle.loads(output)

# Does pickling a function work? Yes it does - and that's why raw pickle received over a network can be hacked
# You unpickle it - it contains a reference to a function - and the function just runs
# That's why never unpickle an untrusted pickle
# Pickles even store references to objects and functions - REMEMBER THAT
def some_function():
    print("This is the output")

function_pickle_output = pickle.dumps(some_function(), protocol=pickle.HIGHEST_PROTOCOL)
function_unpickle_output = pickle.loads(function_pickle_output)

print(some_list)
print(output)
print(back_to_list)
print(function_pickle_output)
print(function_unpickle_output)

