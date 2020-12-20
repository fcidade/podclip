from podclip.robot import Robot, RobotState
import logging

class CutterRobot(Robot):
  
  def run(self, state: RobotState) -> RobotState:
    logging.info(f'Generating clip from "{state.video_path}"')
    logging.info(f'Start: {state.clip_start} End: {state.clip_end}')

    

    logging.info(f'Clip generated on "{state.clip_path}"')
    return state