from typing import List
from podclip.robot import Robot, RobotState
from podclip.robots import (
  UserInputRobot,
  ConfigFileRobot,
  AnalyticsRobot,
  CutterRobot,
  AudioExtractorRobot,
  SpeechRecognizerRobot,
  DescriptionRobot,
  DownloadRobot,
  TagsRobot,
  ThumbnailRobot,
  TittleRobot,
  TwitterRobot,
  UploadRobot,
)

def make_manual() -> List[Robot]:
  return [
    ConfigFileRobot(), #TODO
    DownloadRobot(),
    CutterRobot(),
    ThumbnailRobot(),
    UploadRobot(),
    TwitterRobot(),
  ]

def pipeline():
  print('Starting...')
  
  #robots = [
  #  DownloadRobot(),
  #  AnalyticsRobot(),
  #  CutterRobot(),
  #  AudioExtractorRobot(),
  #  SpeechRecognizerRobot(),
  #  TittleRobot(),
  #  # CoolPhraseForThumbnailRobot(),
  #  DescriptionRobot(),
  #  TagsRobot(),
  #  # CoolestFrame() -> https://github.com/Zulko/moviepy/issues/702
  #  ThumbnailRobot(),
  #  UploadRobot(),
  #  TwitterRobot(),
  #]
  robots = make_manual()
  
  curr_state = RobotState()
  for robot in robots:
    curr_state = robot.run(curr_state)

  print('Finished.')