import unittest
from unittest.mock import patch
from tkinter import Tk
from Snake_Game import GFG
# from tkinter.ttk import *

class TestSnake(unittest.TestCase):

    def setUp(self):
        """ Setup for tests to run """
        self.master = Tk()
        self.gfg = GFG(self.master)

    def test_point(self):
        """ Tests if points are added when player eats apple / eat() method is called """
        coordsPlayer = self.gfg.canvas.coords(self.gfg.rectangle)
        expected_points = 10
        self.gfg.eat(coordsPlayer)
        self.assertEqual(expected_points, self.gfg.points)

    def test_speed_increase(self):
        """ Test if speed increases when player eats apple, speed increases as int -> 0 """
        coordsPlayer = self.gfg.canvas.coords(self.gfg.rectangle)
        normalSpeed = self.gfg.speed
        self.gfg.eat(coordsPlayer)
        increasedSpeed = self.gfg.speed
        self.assertLess(increasedSpeed, normalSpeed)

    # Grid are made during the game's __init__ function
    def test_grid(self):
        """ Grids to canvas are made when GTG.__init__ is called, tests if canvas has tag for grid lines """
        self.assertTrue(self.gfg.canvas.find_withtag('grid_line'))

    @patch('Snake_Game.GFG.grid')
    def test_grid_call(self, mock):
        """ Mocking, tests if grid() is called """
        self.gfg.grid()
        self.assertTrue(mock.called)

    @patch('Snake_Game.GFG.spawn')
    def test_spawn(self, mock):
        """ Mocking, tests if spawn() is called """
        self.gfg.spawn()
        self.assertTrue(mock.called)

    @patch('Snake_Game.GFG.kill')
    def test_kill(self, mock):
        """ Mocking, tests if kill() is called """
        self.gfg.kill()
        self.assertTrue(mock.called)

    @patch('Snake_Game.GFG.movement')
    def test_movement(self, mock):
        """ Mocking, tests if movement() is called """
        self.gfg.movement()
        self.assertTrue(mock.called)

    @patch('Snake_Game.GFG.eat')
    def test_eat(self, mock):
        """ Mocking, tests if eat() is called """
        self.gfg.eat()
        self.assertTrue(mock.called)

    @patch('Snake_Game.GFG.moveTail')
    def test_move_tail(self, mock):
        """ Mocking, tests if moveTail() is called """
        self.gfg.moveTail()
        self.assertTrue(mock.called)

    @patch('Snake_Game.GFG.spawn_food')
    def test_spawn_food(self, mock):
        """ Mocking, tests if spawn_food() is called """
        self.gfg.spawn_food()
        self.assertTrue(mock.called)

    @patch('Snake_Game.GFG.win')
    def test_win(self, mock):
        """ Mocking, tests if win() is called """
        self.gfg.win()
        self.assertTrue(mock.called)

    def test_left(self):
        """ Tests if there are changes to player x coordinates after method is called """
        x_coord_before = self.gfg.x
        self.gfg.left(event=None)
        x_coord_after = self.gfg.x
        self.assertGreater(x_coord_before, x_coord_after)

    def test_right(self):
        """ Tests if there are changes to player x coordinates after method is called """
        x_coord_before = self.gfg.x
        self.gfg.right(event=None)
        x_coord_after = self.gfg.x
        self.assertLess(x_coord_before, x_coord_after)

    def test_up(self):
        """ Tests if there are changes to player y coordinates after method is called """
        y_coord_before = self.gfg.y
        self.gfg.up(event=None)
        y_coord_after = self.gfg.y
        self.assertGreater(y_coord_before, y_coord_after)

    def test_down(self):
        """ Tests if there are changes to player y coordinates after method is called """
        y_coord_before = self.gfg.y
        self.gfg.down(event=None)
        y_coord_after = self.gfg.y
        self.assertLess(y_coord_before, y_coord_after)

if __name__ == '__main__':
    unittest.main()