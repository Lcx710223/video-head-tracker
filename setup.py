### LCX260530 UBUNTU下安装vht,pytorch3d==0.7.3有轮子。其他适配即可。

from setuptools import setup, find_packages

setup(
    name="vht",
    version="0.1.0",
    packages=find_packages(),
    python_requires=">=3.9",
    install_requires=[
        "ConfigArgParse",
        "numpy",
        "scipy",
        "opencv-python",
        "torch==2.0.1",
        "torchvision==0.15.2",
        "pytorch3d==0.7.3",
    ],
)
