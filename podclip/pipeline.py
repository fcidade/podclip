from typing import List
from podclip.robot import Robot, RobotState
from podclip.robots import (
  AnalyticsRobot,
  CutterRobot,
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
    TittleRobot(),
    ThumbnailRobot(),
    DescriptionRobot(),
    TagsRobot(),
    UploadRobot(),
    TwitterRobot(),
  ]
  
  curr_state = RobotState()
  #print(curr_state)
  for robot in robots:
    curr_state = robot.run(curr_state)
    #print(curr_state)

  print('Finished.')