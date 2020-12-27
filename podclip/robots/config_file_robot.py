from podclip.robot import Robot, RobotState
import yaml
import logging

class ConfigFileRobot(Robot):
  
  def run(self, state: RobotState) -> RobotState:
    logging.info('Loading file config...')

    with open('./test/resources/videos/aderiva6.yaml') as f:
      data = yaml.safe_load(f)
      state.youtube_url = data.get('youtube_url')
      state.video_path = data.get('video_path')
      state.clip_path = data.get('clip_path')
      state.clip_start = data.get('clip_start')
      state.clip_end = data.get('clip_end')
      state.thumb_path = data.get('thumb_path')
      state.thumb_frame_path = data.get('thumb_frame_path')
      state.thumb_quote = data.get('thumb_quote')

    logging.info(f'Configuration: {state}')

    return state