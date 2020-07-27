def count_substring(string, sub_string):
    count = sum(1 for i in range(len(string)) if string[i:i+len(sub_string)] == sub_string)
    return count

string = input()
sub_string = input()
print(count_substring(string, sub_string))