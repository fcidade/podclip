from typing import List
from podclip.robot import Robot, RobotState
from podclip.robots import (
  AnalyticsRobot,
  CutterRobot,
  AudioExtractorRobot,
  SpeechRecognizerRobot
  DescriptionRobot,
  DownloadRobot,
  TagsRobot,
  ThumbnailRobot,
  TittleRobot,
  TwitterRobot,
  UploadRobot,
)

def pipeline():
  print('Starting...')
  
  robots: List[Robot] = [
    DownloadRobot(),
    AnalyticsRobot(),
    CutterRobot(),
    AudioExtractorRobot(),
    SpeechRecognizerRobot(),
    TittleRobot(),
    # CoolPhraseForThumbnailRobot(),
    DescriptionRobot(),
    TagsRobot(),
    # CoolestFrame() -> https://github.com/Zulko/moviepy/issues/702
    ThumbnailRobot(),
    UploadRobot(),
    TwitterRobot(),
  ]
  
  curr_state = RobotState()
  for robot in robots:
    curr_state = robot.run(curr_state)

  print('Finished.')