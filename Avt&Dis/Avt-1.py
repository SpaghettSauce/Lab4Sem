def find_substitution(string1, string2):
    substitutions = {'0': '1', '1': '2', '2': '01', '01': '2', '02': '1'}
    if len(string1) != len(string2):
        return False, -1

    count = 0
    for i in range(len(string1)):
        char1 = string1[i]
        char2 = string2[i]

        if char1 != char2:
            if char1 not in substitutions or char2 not in substitutions[char1]:
                return False, -1

            count += 1

    return True, count


string1 = input()
string2 = input()

can_be_obtained, num_substitutions = find_substitution(string1, string2)

if can_be_obtained:
    print("Да")
    print(" ",num_substitutions)
else:
    print("Неа")

