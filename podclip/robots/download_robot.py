from podclip.robot import Robot, RobotState

class DownloadRobot(Robot):
  
  def run(self, state: RobotState) -> RobotState:
    print('Downloading...')
    return state