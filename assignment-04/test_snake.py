from Snake_Game import GFG
import unittest
from unittest.mock import patch
from tkinter import *
from tkinter.ttk import * 


class TestSnake(unittest.TestCase):
    
    def setUp(self):
        self.master = Tk()
        self.gfg = GFG(self.master)
    
    def test_point(self):
        coordsPlayer = self.gfg.canvas.coords(self.gfg.rectangle)
        expected_points = 10
        self.gfg.eat(coordsPlayer)
        self.assertEqual(expected_points, self.gfg.points)
        
    # Speed increases as int -> 0
    def test_speed_increase(self):
        coordsPlayer = self.gfg.canvas.coords(self.gfg.rectangle)
        normalSpeed = self.gfg.speed
        self.gfg.eat(coordsPlayer)
        increasedSpeed = self.gfg.speed
        self.assertLess(increasedSpeed, normalSpeed)
    
    # Grid are made during the game's __init__ function
    def test_grid(self):
        self.assertTrue(self.gfg.canvas.find_withtag('grid_line'))
        
    @patch('Snake_Game.GFG.grid')
    def test_grid_call(self, mock):
        self.gfg.grid()
        self.assertTrue(mock.called)
    
    @patch('Snake_Game.GFG.spawn')
    def test_spawn(self, mock):
        self.gfg.spawn()
        self.assertTrue(mock.called)
        
    @patch('Snake_Game.GFG.kill')
    def test_kill(self, mock):
        self.gfg.kill()
        self.assertTrue(mock.called)
    
    @patch('Snake_Game.GFG.movement')
    def test_movement(self, mock):
        self.gfg.movement()
        self.assertTrue(mock.called)
    
    @patch('Snake_Game.GFG.eat')
    def test_eat(self, mock):
        self.gfg.eat()
        self.assertTrue(mock.called)
        
    @patch('Snake_Game.GFG.moveTail')
    def test_moveTail(self, mock):
        self.gfg.moveTail()
        self.assertTrue(mock.called)
        
    @patch('Snake_Game.GFG.spawn_food')
    def test_spawn_food(self, mock):
        self.gfg.spawn_food()
        self.assertTrue(mock.called)
        
    @patch('Snake_Game.GFG.kill')
    def test_kill(self, mock):
        self.gfg.kill()
        self.assertTrue(mock.called)
        
    @patch('Snake_Game.GFG.win')
    def test_win(self, mock):
        self.gfg.win()
        self.assertTrue(mock.called)
        
    def test_left(self):
        xCoordBefore = self.gfg.x
        self.gfg.left(event=None)
        xCoordAfter = self.gfg.x
        self.assertGreater(xCoordBefore, xCoordAfter)
        
    def test_right(self):
        xCoordBefore = self.gfg.x
        self.gfg.right(event=None)
        xCoordAfter = self.gfg.x
        self.assertLess(xCoordBefore, xCoordAfter)
        
    def test_up(self):
        yCoordBefore = self.gfg.y
        self.gfg.up(event=None)
        yCoordAfter = self.gfg.y
        self.assertGreater(yCoordBefore, yCoordAfter)
        
    def test_down(self):
        yCoordBefore = self.gfg.y
        self.gfg.down(event=None)
        yCoordAfter = self.gfg.y
        self.assertLess(yCoordBefore, yCoordAfter)
        
    
if __name__ == '__main__':
    unittest.main()