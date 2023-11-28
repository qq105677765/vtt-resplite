from setuptools import setup, find_packages

setup(
    name='vtt-resplite',
    version='0.2',
    packages=find_packages(),
    install_requires=[
        # 你的依赖项列表
    ],
    author='wenda zheng',          # 作者
    author_email='105677765@qq.com',  # 作者邮箱
    description='re-splict vtt,srt by ". ! ?"',  # 描述
    long_description='re-splict vtt,srt by ". ! ?"',  # 长描述
    url='https://github.com/qq105677765/vtt-resplite',  # 项目的 URL
    license='MIT',  # 许可证类型
    classifiers=[  # 包的分类标签
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
