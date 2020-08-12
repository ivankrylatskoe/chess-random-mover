# Written by Ivan Bychkov on 12 August 2020
# Email: ivankrylatskoe@gmail.com

import chess
import random
import sys

# UCI commands
UCI_COMMAND = 'uci'
UCI_OK_COMMAND = 'uciok'
IS_READY_COMMAND = 'isready'
READY_OK_COMMAND = 'readyok'
POSITION_COMMAND = 'position' 
MOVES_COMMAND = 'moves'
GO_COMMAND = 'go'
QUIT_COMMAND = 'quit'
BEST_MOVE_COMMAND = 'bestmove'

def write_uci_ok():
    output(UCI_OK_COMMAND)

def write_ready_ok():
    output(READY_OK_COMMAND)

def get_move_list(s):
    move_list = ''
    pos = s.find(MOVES_COMMAND)
    if pos >= 0:
        move_list = s[(pos+len(MOVES_COMMAND)):]
    return move_list

def output_move(move_list):
    board = chess.Board()
    moves = move_list.split(' ')
    for m in moves:
        if m != '':
            board.push_uci(m)
    best_move = random.choice(list(board.legal_moves))
    output(BEST_MOVE_COMMAND + ' ' + best_move.uci())

def log(s, prefix = '>>> '):
    if log_mode:
        f = open("log.txt", "a")
        f.write(prefix + s + '\n')
        f.close()

def output(s):
    print(s)
    log(s, '')

def main(argv):
    global log_mode
    log_mode = False

    print('Chess Random Mover')

    for arg in argv:
        if arg == '--log':
            log_mode = True
        if arg in ('-h', '--help', '-?', '/?'):
            print('Usage: chess-random-mover [--log]')
            print('Use --log parameter to log UCI data')
    
    move_list = ''
    while True:
        s = input()
        log(s)
        commands = s.split(' ')
        if len(commands) == 0:
            continue
            
        if commands[0] == UCI_COMMAND:
            write_uci_ok()
        elif commands[0] == IS_READY_COMMAND:
            write_ready_ok()
        elif commands[0] == POSITION_COMMAND:
            move_list = get_move_list(s)
        elif commands[0] == GO_COMMAND:
            output_move(move_list)
        elif commands[0] == QUIT_COMMAND:
            break
        

if __name__ == '__main__':
    main(sys.argv[1:])
