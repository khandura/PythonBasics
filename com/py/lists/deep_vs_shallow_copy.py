# Deep copy Demo

import copy

orig_list = [1, 4, 6, ['ABC', 'XYZ']]
print("original list before change ", orig_list)

# make a deep copy
deep_copy_list = copy.deepcopy(orig_list)
print("deep copy list before change ", deep_copy_list)

# make a shallow copy
shallow_copy_list = orig_list.copy()
# shallow_copy_list = orig_list[:]
print("shallow copy list before change ", shallow_copy_list)

orig_list[3].append("PPP")
print("original list after change ", orig_list)
print("deep copy list after changing original list ", deep_copy_list)
print("shallow copy list after changing original list ", shallow_copy_list)
