from setuptools import setup

package_name = 'my_first_pkg'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Shahid Ahamed Hasib',
    maintainer_email='shahidhasib586@gmail.com',
    description='A simple publisher-subscriber package in Python',
    license='Apache-2.0',
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    entry_points={
        'console_scripts': [
            'talker_py = my_first_pkg.talker_py:main',
            'listener_py = my_first_pkg.listener_py:main',
        ],
    },
)
