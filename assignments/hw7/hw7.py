

def number_words(in_file_name, out_file_name): # done
    num = 0
    in_file = open(in_file_name, 'r')
    out_file = open(out_file_name, 'w')
    for line in in_file:
        for word in line.split():
            num += 1
            print('{} {}'.format(num, word), sep='\n', file=out_file)

def hourly_wages(in_file_name, out_file_name):
    in_file = open(in_file_name, 'r')
    out_file = open(out_file_name, 'w')
    for line in in_file:
        first, last, hourly, hours = ' '.split(line)
        hourly = hourly + 1.65
        out_list = [first, last, hourly, hours]
        for word in out_list:
            print(word, file=out_file)
            print(sep='/n', file=out_file)


def calc_check_sum(isbn): # done
    isbn = isbn.replace('-', '')
    position = 11
    sum = 0
    for char in isbn:
        position += -1
        sum += eval(char) * position
    return sum





def send_message(file_name, friend_name):
    in_file = open(file_name, 'r')
    out_file_name = '{}.txt'.format(friend_name)
    out_file = open(out_file_name, 'x')
    for line in in_file:
        print(line, sep='\n', file=out_file)


def encode():
    message, key = input('enter a message:'), eval(input('enter a key:'))
    uni = []
    uniconv = []
    convback = []
    for i in message:
        conv1 = ord(i)
        uni.append(conv1)
    for j in uni:
        conv2 = j + key
        uniconv.append(conv2)
    for q in uniconv:
        conv3 = chr(q)
        convback.append(conv3)
    print(''.join(convback))


def send_safe_message(file_name, friend_name, key):
    pass


def send_uncrackable_message(file_name, friend_name, pad_file_name):
    pass


if __name__ == '__main__':
    pass
