# Deepfake Detector App

- [Deepfake Detector App](https://deep-fake-detection-m.streamlit.app/)

## ScreenShots
<img src="https://github.com/Sneh-T-Shah/deepfake-detection/assets/116267467/1cbb8141-7123-4b95-a67d-50f99f3c44bf" width="100" height="100">
![Streamlit - Google Chrome 16-01-2024 21_30_40](https://github.com/Sneh-T-Shah/deepfake-detection/assets/116267467/b2c8e510-3a86-46fa-b022-44fc23846e6d){:height="36px" width="36px"}
![Streamlit - Google Chrome 16-01-2024 21_33_16](https://github.com/Sneh-T-Shah/deepfake-detection/assets/116267467/cf4905a3-0ace-47b5-97e9-e2ecb5ccc89f){:height="36px" width="36px"}

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

## Contact
For any inquiries or feedback, please contact:

- [Sneh shah](https://github.com/Sneh-T-Shah/)
- [Pankil Soni](https://github.com/pankil-soni/)
