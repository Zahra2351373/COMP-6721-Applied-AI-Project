# **COMP6721_Summer2023_G_16**
> *Project:- Age Classification Using Decision Tree, semi supervised and Convolutional Neural Networks*
- [**COMP6721\_Summer2023\_G\_16**](#comp6721_summer2023_g_16)
  - [**Team Formation**](#team-formation)
  - [**Presentation of the project**](#presentation-of-the-project)
  - [**Requirements**](#requirements)
  - [**Guidelines for training/validating the models:**](#guidelines-for-trainingvalidating-the-models)
  - [**Guidelines for accessing the dataset through provided links**](#guidelines-for-accessing-the-dataset-through-provided-links)

## **Team Formation**
1. Anmol Majithia (40216795)
2. Azam Arvin (40171993)
3. Marzieh Adeli(40221843)
4. Zahra Ebrahimi (40169858)

## **Presentation of the project**
- Automated human age classification (HAC) models represent a crucial implementation of facial recognition technology across diverse industries such as marketing and healthcare. Nevertheless, accurately determining an individual's age from their facial features presents a complex challenge for AI systems due to the intricacies associated with interpreting facial images. Previous scholarly works have showcased the effectiveness of deep convolutional neural network (CNN) structures, such as ResNet and custom CNN models, in achieving accurate age classification. However, these models are constrained by their extensive computational demands and reliance on substantial amounts of training data.
 -  In order to tackle these challenges, a systematic approach incorporating decision tree analysis, semi-supervised learning, and the utilization of ResNet and custom models trained on UTKFace datasets was proposed. This study emphasizes the comparison of various models and their performance evaluation, taking into consideration both computational complexity and other relevant factors.
 
## **Requirements**
- numpy               1.24.3
- cv2                 4.7.0
- matplotlib          3.7.1
- torch               2.0.0
- torchvision         0.15.0
- sklearn             1.0.1
- cuda                V11.8 
- PIL                 9.5.0
- pandas              2.0.2
- tqdm                4.65.0
- seaborn             0.12.2
  
## **Guidelines for training/validating the models:**
- ### Decision Trees:
  - Ensure above libraries are installed
  - Download dataset from [this link](https://drive.google.com/file/d/1YVprWQ71r5t_FXNm8DJlPJhvbupwvt4R/view?usp=sharing) and extract in the root folder (sample or complete based on how much processing time you have)
  - Ensure folder name is UTKFace and there are images within it
  - Navigate to "Decision Tree" folder
  - Open one of Supervised/Semisupervised ipynb
  - Ensure path to CSV points to the correct CSV (sample or full dataset, default set to sample)
  - Set **"TRAINING"** flag to *True* if you wish to train the network or *False* if you wish to test it using a pretrained model
  - Run the ipynb!
- ### CNN
  - #### Testing:
    - Ensure above libraries are installed
    - Download dataset from [this link](https://drive.google.com/file/d/1YVprWQ71r5t_FXNm8DJlPJhvbupwvt4R/view?usp=sharing) and extract in the root folder (sample or complete based on how much processing time you have)
    - Ensure folder name is UTKFace and there are images within it
    - Navigate to "Deep Neural Networks" and open any one of the three folders within it, folder name is the type of network we used
    - Within the folder you will find a file starting with "Random_Test_Sample...", open that ipynb and run it to test and validate model!
  - #### Training:
    - To train or validate the code use the network type name ipynb files within "Deep Neural Network/\<Network Type\>"
    - Before running any of those 3 files please change the directory path mentioned in the initial cells.


  
## **Guidelines for accessing the dataset through provided links**
- ### Original Dataset Link:
  - [UTKFace](https://www.kaggle.com/datasets/jangedoo/utkface-new) 
- ### Dataset link after Binary Split:
  - [UTKFace BinarySplit](https://drive.google.com/drive/folders/1Zg627QAMJ5eTo3zNgtBxEgKlbs69VDcY?usp=sharing)

- ### Sample dataset link for Decision Trees:
  - [Sample](https://drive.google.com/file/d/1YVprWQ71r5t_FXNm8DJlPJhvbupwvt4R/view?usp=sharing)