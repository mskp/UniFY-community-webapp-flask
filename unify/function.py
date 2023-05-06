from datetime import datetime
from PIL import Image
import PIL


def time_ago(time):
    """
    Get a datetime object or a int() Epoch timestamp and return a
    pretty string like 'an hour ago', 'Yesterday', '3 months ago',
    'just now', etc
    """
    time = datetime.strptime(time, '%Y-%m-%d %H:%M:%S')
    diff = datetime.now() - time
    second_diff = diff.seconds
    day_diff = diff.days

    if day_diff < 0:
        return ''

    if day_diff == 0:
        if second_diff < 6:
            return "just now"
        if second_diff < 60:
            return str(second_diff) + " seconds ago"
        if second_diff < 120:
            return "a minute ago"
        if second_diff < 3600:
            return str(second_diff // 60) + " minutes ago"
        if second_diff < 7200:
            return "an hour ago"
        if second_diff < 86400:
            return str(second_diff // 3600) + " hours ago"
    if day_diff == 1:
        return "Yesterday"
    if day_diff < 7:
        return str(day_diff) + " days ago"
    if day_diff < 14:
        return "a week ago"
    if day_diff < 31:
        return str(day_diff // 7) + " weeks ago"
    if day_diff < 58:
        return "a month ago"
    if day_diff < 365:
        return str(round(day_diff / 30)) + " months ago"
    if day_diff < 730:
        return "a year ago"
    return str(day_diff // 365) + " years ago"


def resize_image(filename: str) -> any:

    base_width = 1000
    image = Image.open(filename)
    width_percent = (base_width / float(image.size[0]))
    hsize = int((float(image.size[1]) * float(width_percent)))
    image = image.resize((base_width, hsize), Image.LANCZOS)

    return image
