# D-Log-Color-Restore
将DJI pocket3或DJI action4等支持D-log的设备录制的D-log视频文件，批量转换为还原色彩的小工具

这个仓库包含一个Python脚本，该脚本使用FFmpeg批量还原由DJI无人机或手持设备在D-LOG模式下拍摄的视频的色彩。该脚本为用户提供了一个简单的图形用户界面，用户可以选择包含视频的目录，并监视色彩还原过程的进度。

This repository contains a Python script that uses FFmpeg to batch restore the color of videos shot in D-LOG mode by DJI drones. The script provides a simple GUI for users to select the directory containing the videos and monitor the progress of the color restoration process.

## 需求

- Python 3.6 或更高版本
- FFmpeg设置到系统变量

## 安装

1. 克隆此仓库到您的本地机器。
2. 使用pip安装所需的Python包：
3. 确保您的系统上已经安装了FFmpeg。如果没有，您可以从[官方FFmpeg网站](https://ffmpeg.org/download.html)下载。

## 使用

1. 运行脚本：

```bash
python app.py
```

2. 在图形用户界面中，点击“浏览”按钮选择包含您想要还原色彩的D-LOG视频的目录。

3. 点击“开始转换”按钮开始色彩还原过程。进度将在图形用户界面中显示。

还原后的视频将保存在所选目录中名为"色彩还原"的新目录中。

## 注意

此脚本使用FFmpeg的"lut3d"过滤器和一个名为"DJI.cube"的3D LUT文件。请确保此文件与脚本在同一目录中，或者调整脚本以指向"DJI.cube"文件的正确位置。

## 许可证

此项目根据MIT许可证进行许可 - 有关详细信息，请参阅[LICENSE](LICENSE)文件。

## 贡献

本人不会代码，仅GPT生成，欢迎贡献！请随时提交拉取请求。
