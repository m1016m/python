date = raw_input('輸入日期:')
event = raw_input('輸入事件:')
description = raw_input('輸入心得:')
fn = "note.txt"

with open(fn , 'w') as file_obj :
    file_obj.write(date)
    file_obj.write(event)
    file_obj.write(description)