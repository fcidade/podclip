from unittest import TestCase, mock, skip
from unittest.mock import patch
from podclip.robots import ThumbnailRobot
from podclip.robot import RobotState
from os.path import join
import logging

class TestThumbnailRobot(TestCase):

  def test_learning(self):
    prev_state = RobotState(
      thumb_frame=join('test', 'resources', 'videos', 'frame.png'),
      thumb_quote='cool phrase',
      thumb_path=join('test', 'resources', 'videos', 'thumb1.png'),
    )
    state = ThumbnailRobot().run(prev_state)