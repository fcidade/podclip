from unittest import TestCase
from podclip.robots import CutterRobot
from podclip.robot import RobotState

class TestCutterRobot(TestCase):

  def test_(self):
    prev_state = RobotState(
      video_path='resources/videos/teste.mp3',
      clip_start=0,
      clip_end=0,
      clip_path='resources/videos/clip01.mp4'
    )
    state = CutterRobot().run(prev_state)