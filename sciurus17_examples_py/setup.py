import os
from glob import glob

from setuptools import find_packages, setup

package_name = 'sciurus17_examples_py'

setup(
    name=package_name,
    version='0.1.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob(os.path.join('launch', '*launch.[pxy][yma]*'))),
        (os.path.join('share', package_name, 'config'), glob(os.path.join('config', '*'))),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='RT Corporation',
    maintainer_email='shop@rt-net.jp',
    description='python examples of Sciurus17 ROS package',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'pick_and_place_left_arm = sciurus17_examples_py.pick_and_place_left_arm:main',
        ],
    },
)
