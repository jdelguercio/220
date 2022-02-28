from graphics import *

def cipher():
    width = 500
    height = 500
    win = GraphWin("Clicks", width, height)

    message_str, key_str = 'Message to code', 'Enter a keyword'
    message_loc, key_loc = Point(150, 150), Point(150, 180)
    message_inst, key_inst = Text(message_loc, message_str), Text(key_loc, key_str)
    message_inst.draw(win)
    key_inst.draw(win)

    message_entry = Entry(Point(message_loc.getX() + 165, message_loc.getY()), 20)
    key_entry = Entry(Point(key_loc.getX() + 120, key_loc.getY()), 10)
    message_entry.draw(win)
    key_entry.draw(win)

    fake_button = Rectangle(Point(215, 245), Point(285, 275))
    fake_button.draw(win)
    encode_txt = 'Encode'
    encode_text = Text(Point(250, 260), encode_txt)
    encode_text.draw(win)

    result_txt = 'Resulting Message'
    result_text = Text(Point(250, 260),result_txt)

    click_txt = 'Click anywhere to close window'
    click_text = Text(Point(250, 450), click_txt)

    win.getMouse()

    fake_button.undraw()
    encode_text.undraw()

    message, key = message_entry.getText(), key_entry.getText()

    message = message.split(sep=' ')
    message = ''.join(message)
    message = message.upper()
    key = key.upper()
    key = (key * (len(message) // len(key) + 1))[:len(message)]
    key_list, message_list = list(key), list(message)

    key_list_uni = []
    message_list_uni = []
    output_ord = []
    output_char = []

    for i in key_list:
        uni_keyk = ord(i) - 65
        key_list_uni.append(uni_keyk)
    for j in message_list:
        uni_keym = ord(j) - 65
        message_list_uni.append(uni_keym)
    for q in range(0, len(message)):
        key_combine = (key_list_uni[q] + message_list_uni[q]) % 26
        output_ord.append(key_combine)
    for z in output_ord:
        out_char = chr(z + 65)
        output_char.append(out_char)
    out_string = ''.join(output_char)

    out_text = Text(Point(250,275),out_string)
    out_text.draw(win)
    result_text.draw(win)
    click_text.draw(win)

    win.getMouse()
    win.close()

cipher()

