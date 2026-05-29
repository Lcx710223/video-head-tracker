from setuptools import setup, find_packages

setup(
    name="vht",
    version="0.1.0",
    packages=find_packages(),
    python_requires=">=3.9",
    install_requires=[
        "ConfigArgParse",
        "matplotlib",
        "scipy",
        "opencv-python",
        "face-alignment",
        "face-detection-tflite",
        "trimesh",
        "pyrender",
    ],
)
