"""PIL based font support for p5.

:author: Abhik Pal
:date: 2018-07

"""
import contextlib
import functools
import textwrap

import PIL
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

__all__ = ['create_font', 'load_font', 'text', 'text_font', 'render_font']

_rendering = False
_canvas = None
_canvas_draw = None

_font_family = ImageFont.load_default()

def _ensure_rendering(func):
    """Ensure that rendering mode is enabled.
    """
    @functools.wraps(func)
    def rfunc(*args, **kwargs):
        if not _rendering:
            fname = func.__name__
            err_msg = "{} can only be called with rendering enabled"
            raise ValueError(err_msg.format(fname))
        return func(*args, **kwargs)
    return rfunc

def create_font(name, size):
    """Create the given font at the appropriate size.

    """
    if name.endswith('ttf'):
        _font_family = ImageFont.truetype(name, size)
    elif name.endswith('pil'):
        _font_family = ImageFont.load(name)
    else:
        raise NotImplementedError("Font type not supported.")

    return _font_family

def load_font(font_name):
    """Loads the given font into a font object

    :rtype: PIL.ImageFont.

    """
    return create_font(font_name, 10)

@_ensure_rendering
def text(text_string, position, wrap_at=None):
    """Draw the given text on the screen and save the image.

    :param text_string: text to display
    :type text_string: str

    :param position: position of the text on the screen
    :type position: tuple

    :param wrap_at: specifies the text wrapping column (defaults to
        None)
    :type wrap_at: int

    :returns: actual text that was drawn to the image (when wrapping
        is not set, this is just the unmodified text_string)
    :rtype: str

    """
    if not (wrap_at is None):
        text_string = textwrap.fill(text_string, wrap_at)
    _canvas_draw.text(position, text_string, font=_font_family)
    return text_string

def text_font(font):
    """Set current text font.

    :param font:
    :type font: PIL.ImageFont.ImageFont

    """
    global _font_family
    _font_family = font

@contextlib.contextmanager
def render_font(size=(640, 260), filename='pfont-test.png'):
    global _canvas
    global _canvas_draw
    global _rendering

    _canvas = Image.new('RGB', size, color=(51, 51, 51))
    _canvas_draw = ImageDraw.Draw(_canvas)
    _rendering = True

    yield

    _rendering = False
    _canvas.save(filename)
