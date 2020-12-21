from unittest import TestCase, mock, skip
from unittest.mock import patch
from podclip.robots import AudioExtractorRobot
from podclip.robot import RobotState
from os.path import join
import logging

class TestAudioExtractorRobot(TestCase):

  @skip
  def test_convert_called_with_right_parameters(self):
    prev_state = RobotState(
      clip_path=join('test', 'resources', 'videos', 'clip0.mp4'),
      clip_audio_path=join('test', 'resources', 'videos', 'clip0-audio.wav'),
    )
    with patch('podclip.robots.audio_extractor_robot.mp.VideoFileClip') as m:
      state = AudioExtractorRobot().run(prev_state)

  @skip
  def test_learning(self):
    prev_state = RobotState(
      clip_path=join('test', 'resources', 'videos', 'clip1.mp4'),
      clip_audio_path=join('test', 'resources', 'videos', 'clip1-audio.wav'),
    )
    state = AudioExtractorRobot().run(prev_state)