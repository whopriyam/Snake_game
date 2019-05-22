import random
import curses


s = curses.initscr()
curses.curs_set(0)
h, w = s.getmaxyx()
p = curses.newwin(h, w, 0, 0)
p.keypad(1)
p.timeout(50)


snake_x = w/2
snake_y = h/4
snake = [
    [snake_y, snake_x],
    [snake_y, snake_x-1],
    [snake_y, snake_x-2]
]


food = [h/7, w/7]
p.addch(food[0], food[1], curses.ACS_STERLING)


key = curses.KEY_RIGHT


while True:
    next_key = p.getch()
    key = key if next_key == -1 else next_key


    if snake[0][0] in [0, h] or snake[0][1]  in [0, w] or snake[0] in snake[1:]:
        curses.endwin()
        quit()


    new_head = [snake[0][0], snake[0][1]]


    if key == curses.KEY_DOWN:
        new_head[0] += 1
    if key == curses.KEY_UP:
        new_head[0] -= 1
    if key == curses.KEY_LEFT:
        new_head[1] -= 1
    if key == curses.KEY_RIGHT:
        new_head[1] += 1


    snake.insert(0, new_head)


    if snake[0] == food:
        food = None
        while food is None:
            nf = [
                random.randint(1, h-1),
                random.randint(1, w-1)
            ]
            food = nf if nf not in snake else None
        p.addch(food[0], food[1], curses.ACS_STERLING)
    else:
        tail = snake.pop()
        p.addch(tail[0], tail[1], ' ')


    p.addch(snake[0][0], snake[0][1], curses.ACS_CKBOARD)
