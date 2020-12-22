from unittest import TestCase, mock, skip
from unittest.mock import patch
from podclip.robots import UserInputRobot
from podclip.robot import RobotState
from os.path import join
import logging

class TestUserInputRobot(TestCase):

  @skip
  def test_learning(self):
    prev_state = RobotState(
    )
    state = UserInputRobot().run(prev_state)