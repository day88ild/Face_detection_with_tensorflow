# Face Detection Project

This project is an experiment in face detection using TensorFlow. It includes a custom architecture for face detection, training scripts, and an inference script for real-time face detection. The project structure is as follows:

## Project Structure

- **/data**: This directory contains the dataset used for training and inference.
  - **/my_data_in_progress**: Placeholder for your data in progress.
  - **/the_main_data_yolo**: Main dataset for YOLO-based face detection.
    - **/full**: Contains the full dataset for face detection.
      - **/images**:
        - **/train**: Training images
        - **/val**: Validation images
      - **/labels**:
        - **/train**: Training labels
        - **/val**: Validation labels
    - **/part1** to **/part6**: Subsets of the main dataset, if applicable.
      - **/images** and **/labels**: Similar to the structure in `/full`.

- **/README.md**: This file, providing an overview of the project.

- **/getting_my_data.ipnb**: Jupyter Notebook for collecting and organizing data.

- **/model_training.ipnb**: Jupyter Notebook for training custom face detection models.

- **/models**: Directory for storing trained face detection models.
  - **model_face_detection_01.h5**: Trained face detection model 01.
  - **model_face_detection_02.h5**: Trained face detection model 02.

- **/inference.py**: Python script for real-time face detection using a trained model.

- **/requirements.txt**: List of Python dependencies required for the project.

## Data

Unfortunately it is impossible to load the data I trained my models on due to Github limitations
but here you can find a link to it on Kaggle (https://www.kaggle.com/datasets/fareselmenshawii/face-detection-dataset). 

## Project Usage

1. **Data Collection**: Use `getting_my_data.ipnb` to collect and organize your data in `/data`.

2. **Model Training**: Train custom face detection models using `model_training.ipnb` and save them in the `/models` directory.

3. **Inference**: Run `inference.py` to perform real-time face detection using a trained model.


## Notes

This project uses pure TensorFlow for experimentation purposes.
The project structure follows a clear organization of data, code, and trained models.

## Dependencies

Ensure you have the required Python packages installed by running:

```bash
pip install -r requirements.txt


