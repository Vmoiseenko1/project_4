# Individual project 4
# Developer: Moiseenko Victoria

import turtle as tr
import math as mth
import random


class Ufo:
    def __init__(self, name, x, y, size, color, count_pillars, count_lamps, pillars_down=True, show_name=True,
                 made_in='Russia', engine_grade='Turbo UFO', speed=10):

        self.__name = name
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.count_pillars = count_pillars
        self.count_lamps = count_lamps
        self.pillars_down = pillars_down
        self.show_name = show_name
        self.speed = speed
        self.__made_in = made_in
        self.__engine_grade = engine_grade
        self.__direction = 360 * random.random()

    @property
    def engine_grade(self):
        return self.__engine_grade

    @engine_grade.setter
    def engine_grade(self, new_grade):
        if new_grade == '':
            print('Марка двигателя не может быть пустой строкой')
        else:
            self.__engine_grade = new_grade

    @engine_grade.getter
    def engine_grade(self):
        if self.__engine_grade == 'Turbo UFO':
            return 'По умолчанию'
        else:
            return self.__engine_grade

    @property
    def set_made_in(self, made_in):
        countries = ['USA', 'Russia']
        if made_in in countries:
            self.__made_in = made_in
        else:
            self.__made_in = None

    @property
    def get_made_in(self):
        return self.__made_in

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def show(self, porthole_color='blue', lamps_color='yellow'):
        if self.pillars_down:
            for i in range(self.count_pillars):
                lx = self.x - self.size / 2 + i * (self.size / (self.count_pillars - 1))
                tr.penup()
                tr.goto(self.x, self.y + self.size / 3)
                tr.pendown()
                tr.goto(lx, self.y - self.size / 6)

        tr.penup()
        tr.goto(self.x, self.y - self.size / 12)
        tr.pendown()
        tr.fillcolor(porthole_color)
        tr.begin_fill()
        tr.circle(self.size / 4)
        tr.end_fill()

        tr.penup()
        tr.fillcolor(self.color)
        tr.goto(self.x - self.size / 2, self.y + self.size / 4)
        tr.pendown()
        tr.begin_fill()
        tr.forward(self.size)
        i = mth.pi / 2
        while i <= 3 * mth.pi / 2:
            sx = (self.size / 2) * mth.sin(i)
            sy = (self.size / 3) * mth.cos(i)
            tr.goto(self.x + sx, self.y + self.size / 4 + sy)
            i += mth.pi / self.size
        tr.end_fill()

        tr.fillcolor(lamps_color)
        n = self.count_lamps + 2
        for i in range(1, n - 1):
            dx = self.size / (n - 1)
            tr.begin_fill()
            tr.penup()
            tr.goto(self.x - self.size / 2 + i * dx, self.y + self.size / 14)
            tr.pendown()
            tr.circle(dx / 4)
            tr.end_fill()

        if self.show_name:
            tr.penup()
            tr.goto(self.x, self.y + self.size / 2)
            tr.pendown()
            tr.write(self.__name, align='center')

    def hide(self, bg_color='white'):
        color = self.color
        self.color = bg_color
        tr.pencolor('white')
        self.show(porthole_color=bg_color, lamps_color=bg_color)
        self.hide_name()
        tr.pencolor('black')
        self.color = color

    def hide_name(self, bg_color='white', font_size=10):
        tr.penup()
        tr.goto(self.x - len(self.__name) / 2 * font_size, self.y + self.size / 2)

        tr.fillcolor(bg_color)
        tr.begin_fill()
        tr.lt(90)
        tr.fd(font_size)
        tr.rt(90)
        tr.fd(font_size * len(self.__name))
        tr.rt(90)
        tr.fd(font_size)
        tr.rt(90)
        tr.fd(font_size * len(self.__name))
        tr.lt(180)
        tr.end_fill()

        tr.pendown()

    def random_move(self, max_direction_change=60):
        direction_change = max_direction_change * random.uniform(-1, 1)
        self.__direction += direction_change
        dx = mth.cos(self.__direction) * self.speed
        dy = mth.sin(self.__direction) * self.speed
        self.x += dx
        self.y += dy

    def random_travel(self):
        self.hide()
        self.random_move()
        self.show()

    def __str___(self):
        if self.show_name:
            s = '\nСконструировано НЛО под названием ' + self.__name + '\n'
        else:
            s = '\nНазвание неизвестно' + '\n'

        s += 'Координаты (' + str(self.x) + ', ' + str(self.y) + ')\n'
        s += 'Размер: ' + str(self.size) + '\n'
        s += 'Цвет ' + self.color + '\n'
        s += str(self.count_pillars) + ' лап\n'
        s += str(self.count_lamps) + ' ламп\n'

        if self.pillars_down:
            s += 'Опоры опущены'
        else:
            s += 'Опоры подняты'
        return s

    def __repr__(self):
        return self.__str___()





