from podclip.robot import Robot, RobotState
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
import logging

class CutterRobot(Robot):
  
  def run(self, state: RobotState) -> RobotState:
    logging.info(f'Generating clip from "{state.video_path}"')
    logging.info(f'Start: {state.clip_start}s End: {state.clip_end}s')

    ffmpeg_extract_subclip(
      state.video_path, 
      state.clip_start, state.clip_end, 
      targetname=state.clip_path
    )

    logging.info(f'Clip generated on "{state.clip_path}"')
    return state