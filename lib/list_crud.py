def create_an_empty_list():
    return []

def create_a_list():
    return [1,2,'Joy','run']

def add_element_to_end_of_list(my_list, element):
    my_list.append(element)
    return my_list

def add_element_to_start_of_list(new_list, element):
    new_list.insert(0,element)
    return new_list

def remove_element_from_end_of_list(list_remove):
    list_remove.pop()
    return list_remove

def remove_element_from_start_of_list(list_del): 
    del list_del[0]
    return list_del

def retrieve_first_element_from_list(list_return):
    return list_return[0]

def retrieve_element_from_index(list_retrieve, index):
    return list_retrieve[1]

def retrieve_last_element_from_list(retrieve_last_element):
    return retrieve_last_element[-1]
