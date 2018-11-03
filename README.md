# HEFRSys
A high-efficiency Facial Recognition system developed for a research project.  

# Details 
HEFRSys is an abbreviation of *High-Efficiency Facial Recognition System*.  Currently, most Facial Recognition models require a massive amount of high-quality data to function at a considerable level, but such ideal datasets are not available to us most of the time.  Therefore, I've worked on a project to develop a Facial Recognition model which performs moderately well despite being trained on realistic data. 

## Requirements
* Python 3.6
* OpenCV 3.3+

### Directory Layout for image data

    .
    ├── functions
    ├── data                 # Data for training
    │   ├── convict          # Put your convict images here
    │   ├── civilian         # Put your civilian images here
    └── ...
