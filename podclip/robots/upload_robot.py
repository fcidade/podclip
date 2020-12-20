from podclip.robot import Robot, RobotState

class UploadRobot(Robot):
  
  def run(self, state: RobotState) -> RobotState:
    print('Uploading to Youtube...')
    return state