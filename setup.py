"""Setup for zoom_meeting XBlock."""


import os

from pathlib import Path
from setuptools import setup


this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()


def package_data(pkg, roots):
    """Generic function to find package_data.

    All of the files under each of the `roots` will be declared as package
    data for package `pkg`.

    """
    data = []
    for root in roots:
        for dirname, _, files in os.walk(os.path.join(pkg, root)):
            for fname in files:
                data.append(os.path.relpath(os.path.join(dirname, fname), pkg))

    return {pkg: data}


setup(
    name='zoom-meeting-xblock',
    version='0.1',
    description='XBlock to use Zoom Meeting.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/edly-io/zoom-meeting-xblock',
    license='MIT',
    author='edly',
    author_email='hello@edly.io',
    keywords='python edx zoom meeting xblock',
    packages=[
        'zoom_meeting',
    ],
    install_requires=[
        'XBlock',
    ],
    entry_points={
        'xblock.v1': [
            'zoom_meeting = zoom_meeting:ZoomMeetingXBlock',
        ]
    },
    package_data=package_data("zoom_meeting", ["static", "public"]),
)
