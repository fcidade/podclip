from podclip.robot import Robot, RobotState

class ThumbnailRobot(Robot):
  
  def run(self, state: RobotState) -> RobotState:
    print('Generating Thumbnail...')
    return state