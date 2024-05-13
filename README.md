# Deepfake Detector App

- [Deepfake Detector App](https://deep-fake-detection-m.streamlit.app/)

## ScreenShots
![Streamlit - Google Chrome 16-01-2024 21_30_24](https://github.com/Sneh-T-Shah/deepfake-detection/assets/116267467/eccce6cc-b829-4f68-9dda-42da833a571a)
![Streamlit - Google Chrome 16-01-2024 21_30_40](https://github.com/Sneh-T-Shah/deepfake-detection/assets/116267467/33e35488-d1ef-4c9a-825f-c2a1be5bae89)
![Streamlit - Google Chrome 16-01-2024 21_50_22](https://github.com/Sneh-T-Shah/deepfake-detection/assets/116267467/4a2007ff-aeb4-48da-b4c6-2cec40b0ba89)
![Streamlit - Google Chrome 16-01-2024 21_33_16](https://github.com/Sneh-T-Shah/deepfake-detection/assets/116267467/f3b42776-d7a6-4563-8fae-60abc4623965)

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [File Structure](#file-structure)
- [Dependencies](#dependencies)
- [Contributing](#contributing)
- [Acknowledgments](#acknowledgments)
- [Contact](#contact)

## Introduction

Welcome to the Deepfake Detector App repository! This Streamlit app is designed to detect deepfake content in images and videos using state-of-the-art models. It provides a user-friendly interface for uploading files and obtaining deepfake predictions with adjustable parameters.

# Recommended parameters:
 - Model : **EfficientNetAutoAttB4**
 - Dataset: **DFDC**

## Features

- **File Type Selection**: Choose between uploading an image or a video for deepfake detection.
- **Model Selection**: Select from various deepfake detection models, such as EfficientNetB4, EfficientNetB4ST, EfficientNetAutoAttB4, etc.
- **Dataset Option**: Choose the dataset (DFDC or FFPP) used to train the deepfake detection model.
- **Adjustable Threshold**: Set a threshold for deepfake probability to control sensitivity.
- **Video Frame Selection**: If analyzing a video, choose the number of frames to process.
- **Detailed Results**: Get detailed results with probabilities and visual cues indicating the likelihood of deepfake content.
- **Project Information**: Display additional information about the project, such as credits, links to GitHub, and collaborators.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/Sneh-T-Shah/deepfake-detection.git
cd deepfake-detection
```

2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run the Streamlit app:
```bash
streamlit run app.py
```
Visit the provided local URL to access the app in your browser.

## File Structure
- app.py : Main Streamlit application script.
- api.py : Contains functions for processing images and videos using deepfake detection models.
- uploads/ : Folder to store uploaded files.
- requirements.txt : List of Python dependencies.

## Dependencies

Find the dependencies here: https://github.com/Sneh-T-Shah/deepfake-detection/blob/main/requirements.txt

## Contributing
We welcome contributions! If you'd like to contribute to this project.


## Acknowledgments
Web app for this project is made by Sneh Shah and Pankil Soni.

The original source for the deep-learning models is on the github reopsitory https://github.com/polimi-ispl/icpr2020dfdc

## Contact
For any query or feedback, please contact:

- [Sneh shah](https://github.com/Sneh-T-Shah/)
- [Pankil Soni](https://github.com/pankil-soni/)
