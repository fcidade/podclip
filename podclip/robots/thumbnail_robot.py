from podclip.robot import Robot, RobotState
from typing import Tuple
from PIL import Image, ImageDraw, ImageFont
import logging
import textwrap

"""
  Cool pallettes:
  - https://lospec.com/palette-list/borkfest
  - https://lospec.com/palette-list/bloody
"""

class ThumbnailRobot(Robot):

  def __init__(self):
    self.width = 1280
    self.height = 720
    self.pd = 10
  
  def run(self, state: RobotState) -> RobotState:
    logging.info(f'Generating Thumbnail w/ frame "{state.thumb_frame_path}" and quote "{state.thumb_quote}"...')

    thumbnail = Image.new('RGB', self.dimensions, color='#e9345a')
    frame = Image.open(state.thumb_frame_path, 'r')
    frame = frame.resize(self.frame_with_padding)


    thumbnail.paste(frame, self.frame_pivot)
    frame.close()

    self.draw_text(thumbnail, state.thumb_quote)
 
    thumbnail.save(state.thumb_path)

    logging.info(f'Thumbnail saved on "{state.thumb_path}"')
    return state

  def draw_text(self, img: Image, text: str):
    font = ImageFont.truetype(r'fonts/Roboto/Roboto-Black.ttf', 116)
    draw = ImageDraw.Draw(img)

    for i, phrase in enumerate(textwrap.wrap(text, width=18)):
      draw.text(
          self.text_pivot(i),
          phrase,
          font=font,
          anchor='mm',
        )

  def text_pivot(self, index: int = 0) -> Tuple[int]:
    return self.width // 2, 500 + index * 100

  @property
  def dimensions(self) -> Tuple[int]:
    return (self.width, self.height)

  @property
  def frame_with_padding(self) -> Tuple[int]:
    return (self.width - (self.pd * 2), self.height - (self.pd * 2))

  @property
  def frame_pivot(self) -> Tuple[int]:
    return (self.pd, self.pd)