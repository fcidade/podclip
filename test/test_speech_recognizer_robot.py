from unittest import TestCase, mock, skip
from podclip.robots import SpeechRecognizerRobot
from podclip.robot import RobotState
from os.path import join
import logging

class TestSpeechRecognizerRobot(TestCase):

  def setUp(self):
    logging.basicConfig(level=logging.INFO, format='%(message)s')

  @skip
  def test_subclip_called_with_right_parameters(self):
    prev_state = RobotState(
      clip_audio_path=join('test', 'resources', 'videos', 'clip0-audio.wav'),
      language='pt-BR',
    )
    with mock.patch('podclip.robots.cutter_robot.ffmpeg_extract_subclip') as m:
      state = SpeechRecognizerRobot().run(prev_state)
      
  @skip
  def test_learning(self):
    prev_state = RobotState(
      clip_audio_path=join('test', 'resources', 'videos', 'clip1-audio.wav'),
      language='pt-BR',
    )
    state = SpeechRecognizerRobot().run(prev_state)
      