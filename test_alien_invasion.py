# Testing the classes in the Alien Invasion project
import unittest
from unittest.mock import Mock
from unittest.mock import patch
import pygame
import pathlib as pl
from settings import Settings
from alien_invasion import AlienInvasion
from ship import Ship


# Test Settings if lives are set at 3
class TestSettings(unittest.TestCase):
    def setUp(self):
        self.my_settings = Settings()

    def test_default_lives(self):
        msg_ship_lives = "Wrong number of backup ships"
        self.assertEqual(self.my_settings.ship_limit, 3, msg_ship_lives)


# Test if the images are in the right folder
class TestPathBase(unittest.TestCase):
    def assertIsFile(self, path):
        if not pl.Path(path).resolve().is_file():
            raise AssertionError("File does not exist: %s" % str(path))

class TestImages(TestPathBase):
    def testShipImage(self):
        ship_path = pl.Path('images/ship.bmp')
        self.assertIsFile(ship_path)
    def testAlienImage(self):
        alien_path = pl.Path('images/alien.bmp')
        self.assertIsFile(alien_path)


# Test ship class - ship initial position
class TestShip(unittest.TestCase):
    def setUp(self):
        self.my_AIgame = AlienInvasion()
        self.my_ship = Ship(self.my_AIgame)

    def test_ship_default_positions(self):
        ship_width = 60
        ship_height = 48
        msg_ship_position = "Ship is not in the bottom middle of 1920X1080 screen"
        self.assertEqual(self.my_ship.rect.x, 1920/2 - ship_width/2, msg_ship_position)
        self.assertEqual(self.my_ship.rect.y, 1080 - ship_height, msg_ship_position)


# Test AlienInvasion class
class TestAlienInvasion(unittest.TestCase):
    def setUp(self):
        self.my_AIgame = AlienInvasion()
    
    # background music should be off before run_game()
    def test_background_music_off(self):
        msg_background_music_off = "Why background music is on before run it?!"
        self.assertFalse(pygame.mixer.music.get_busy(), msg_background_music_off)

    # test if the "Failed!" text display is succesfully called in gameover()
    @patch("alien_invasion.AlienInvasion.text_display")
    def test_gameover(self, mock_over):
        self.assertFalse(mock_over.called)
        self.my_AIgame.gameover()
        self.assertTrue(mock_over.called)
        # self.assertEqual(mock_over.call_count, 1)


# Main
if __name__ == '__main__':
    unittest.main(verbosity=2)