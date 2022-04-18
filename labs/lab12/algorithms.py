
def read_data(filename):
    file = open(filename, 'r')
    line_list = list(file.readlines())
    count = 0
    output = []

    while count < len(line_list):
        nums = line_list[count].split()
        i = 0
        while i < len(nums):
            output.append(int(nums[i]))
            i += 1
        count += 1

    file.close()
    return output

def is_in_linear(search_val, values):
    answer = search_val in values
    return answer





