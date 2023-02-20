""" turtle_demo.py

"""
import turtle as t


def draw_star(distance: int, angle: int) -> None:
    t.color('red', 'yellow')
    t.begin_fill()
    while True:
        t.forward(distance)
        t.left(angle)
        if abs(t.pos()) < 1:
            break
    t.end_fill()
    t.done()


if __name__ == "__main__":
    draw_star(200, 170)
