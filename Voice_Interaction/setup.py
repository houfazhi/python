from setuptools import setup, find_packages

setup(
    name='Voice_Interaction',
    version='1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'speech_recognition',
        'aip',
        'pyttsx3',
        # Add other dependencies here
    ],
    entry_points={
        'console_scripts': [
            'my_voice_recognition = your_module:main',  # Replace with your entry point
        ],
    },
    author='Hou',
    author_email='2775313450@qq.com',
    description='a simple Voice_Interaction package',
    url='https://github.com/your_username/your_project',
)
