from setuptools import setup, find_packages


setup(
    name='beep-reader-player',
    version='1.1.0',
    description='',
    author='Antti Juvonen',
    packages=find_packages(),
    python_requires='>=3.6',
    install_requires=['numpy','pygame'],
    tests_require=['pytest'],
    setup_requires=['pytest-runner'],
    entry_points = {
        'console_scripts': [
            'beep-reader-player=beep_reader_player.beep_reader_player:main'
            ]
        }
)
