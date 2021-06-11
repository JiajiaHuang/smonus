import os.path
import uuid


def generate_uuid4_filename(filename):
    discard, ext = os.path.splitext(filename)

    basename = uuid.uuid4()
    return u'{0}{1}'.format(basename, ext)
