# D-Log-Color-Restore
将DJI pocket3或DJI action4等支持D-log的设备录制的D-log视频文件，批量转换为还原色彩的小工具

# DJI D-LOG Video Color Restoration

This repository contains a Python script that uses FFmpeg to batch restore the color of videos shot in D-LOG mode by DJI drones. The script provides a simple GUI for users to select the directory containing the videos and monitor the progress of the color restoration process.

## Requirements

- Python 3.6 or higher
- FFmpeg
- tkinter

## Installation

1. Clone this repository to your local machine.
2. Install the required Python packages using pip:

```bash
pip install -r requirements.txt
```

3. Make sure FFmpeg is installed on your system. If not, you can download it from the [official FFmpeg website](https://ffmpeg.org/download.html).

## Usage

1. Run the script:

```bash
python app.py
```

2. In the GUI, click the "Browse" button to select the directory containing the D-LOG videos you want to restore color to.

3. Click the "Start Conversion" button to start the color restoration process. The progress will be displayed in the GUI.

The restored videos will be saved in a new directory named "色彩还原" within the selected directory.

## Note

This script uses the "lut3d" filter of FFmpeg with a 3D LUT file named "DJI.cube". Make sure this file is in the same directory as the script or adjust the script to point to the correct location of the "DJI.cube" file.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
