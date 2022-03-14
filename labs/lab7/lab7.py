def weighted_average(in_file_name, out_file_name):
    in_file = open(in_file_name, 'r')
    out_file = open(out_file_name, 'w')
    class_avg = []
    for line in in_file:
        input_list = []
        for word in line.split(':'):
            input_list.append(word)
        input_list[1] = input_list[1].strip()
        math_list = []
        for num in input_list[1].split(' '):
            num = eval(num)
            math_list.append(num)
            grades = []
            weights = []
        for i in range(len(math_list)):
            if i % 2:
                grades.append(math_list[i])
            else:
                weights.append(math_list[i])
        numerator = 0
        for i in range(len(grades)):
            numerator += grades[i] * weights[i]
            if sum(weights) == 100:
                avg = numerator / 100
            elif sum(weights) > 100:
                avg = 'Error: The weights are greater than 100.'
            else:
                avg = 'Error: The weights are less than 100.'
        if type(avg) == str:
            pass
        else:
            class_avg.append(avg)
        print("{}'s average: {}".format(input_list[0], avg), file=out_file)
    class_avg = sum(class_avg) / len(class_avg)
    print('Class average: {}'.format(class_avg), file=out_file)

def main():
    in_file_name = 'grades.txt'
    out_file_name = 'avg.txt'
    weighted_average(in_file_name, out_file_name)

main()