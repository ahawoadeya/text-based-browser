import os
import sys
from collections import deque

nytimes_com = '''
This New Liquid Is Magnetic, and Mesmerizing

Scientists have created “soft” magnets that can flow 
and change shape, and that could be a boon to medicine 
and robotics. (Source: New York Times)


Most Wikipedia Profiles Are of Men. This Scientist Is Changing That.

Jessica Wade has added nearly 700 Wikipedia biographies for
 important female and minority scientists in less than two 
 years.

'''

bloomberg_com = '''
The Space Race: From Apollo 11 to Elon Musk

It's 50 years since the world was gripped by historic images
 of Apollo 11, and Neil Armstrong -- the first man to walk 
 on the moon. It was the height of the Cold War, and the charts
 were filled with David Bowie's Space Oddity, and Creedence's 
 Bad Moon Rising. The world is a very different place than 
 it was 5 decades ago. But how has the space race changed since
 the summer of '69? (Source: Bloomberg)


Twitter CEO Jack Dorsey Gives Talk at Apple Headquarters

Twitter and Square Chief Executive Officer Jack Dorsey 
 addressed Apple Inc. employees at the iPhone maker’s headquarters
 Tuesday, a signal of the strong ties between the Silicon Valley giants.
'''

# write your code here
args = sys.argv
tb_tabs = args[1]


def create_dir():
    if tb_tabs:
        try:
            os.mkdir(tb_tabs)
        except FileExistsError:
            pass


def save_web_files(filename, content):
    parent_dir = '/home/derts/PycharmProjects/Text-Based Browser/Text-Based Browser/task/tb_tabs'
    with open(os.path.join(parent_dir, filename), 'w') as open_file:
        open_file.write(content)


def read_web_files(filename):
    parent_dir = '/home/derts/PycharmProjects/Text-Based Browser/Text-Based Browser/task/tb_tabs'
    with open(os.path.join(parent_dir, filename), 'r') as open_file:
        print(open_file.read())


create_dir()
deque_web_stack = deque([])

while True:
    data_input = input('')

    if data_input == 'bloomberg.com':
        print(bloomberg_com)
        save_web_files('bloomberg.txt', bloomberg_com)
        deque_web_stack.append(bloomberg_com)
        if data_input == 'bloomberg':
            read_web_files('bloomberg.txt')
    elif data_input == 'nytimes.com':
        print(nytimes_com)
        save_web_files('nytimes.txt', nytimes_com)
        deque_web_stack.append(nytimes_com)
        if data_input == 'nytimes':
            read_web_files('nytimes.txt')
    elif data_input == 'back':
        try:
            print(deque_web_stack.popleft())
        except IndexError:
            pass
    elif data_input == 'exit':
        exit()
    else:
        print('Error: Incorrect URL')
