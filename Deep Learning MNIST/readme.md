# Extended Neural Network for Digit Recognition

A multi-layer neural network implementation for handwritten digit recognition using the MNIST dataset.

## Introduction

This project implements an extended neural network with three layers to classify handwritten digits. It uses the MNIST dataset for training and evaluation. The network is built from scratch using NumPy and demonstrates key concepts in deep learning such as forward propagation, backpropagation, and gradient descent.

**Keywords**: Neural Network, Deep Learning, MNIST, Digit Recognition, Python, NumPy

## User Instructions

### Installation

1. Clone the repository:
   ```
   git clone https://github.com/ajaychary06/Projects.git
   cd Projects/Deep-Learning-MNIST/
   ```

2. Install the required dependencies:
   ```
   pip install numpy pandas matplotlib
   ```

3. Download the MNIST dataset and place it in the project directory.

## Developer Instructions

### Building and Running the Project

1. Ensure you have Python 3.x installed.
2. Install the required libraries as mentioned in the Installation section.
3. Open and run the Jupyter notebook `extended_network.ipynb`.
4. The notebook contains all the necessary code to train the model and evaluate its performance.

## Results

The extended neural network achieves an accuracy of approximately 78.58% on the training set after 200 iterations. The model demonstrates steady improvement in both loss reduction and accuracy increase throughout the training process.

## Methodologies

- Data Preprocessing: Normalization of pixel values
- Model Architecture: 3-layer neural network (784 -> 64 -> 10 -> 10)
- Activation Functions: ReLU for hidden layers, Softmax for output layer
- Loss Function: Cross-entropy loss
- Optimization: Gradient descent with customizable learning rate

## Expectations

This project is expected to serve as a learning tool for understanding the fundamentals of neural networks and their implementation from scratch. While it achieves reasonable accuracy, it is not intended to compete with state-of-the-art models for digit recognition.


## Citations:
[1] https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/51974993/96a2d750-aadd-44a3-8010-c22337817c4a/extended_network.ipynb

[2] https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/51974993/e2a1dde5-1a6b-42f1-b414-c457d64917a7/original_network.ipynb

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/ajaychary06/Projects/blob/main/LICENSE) file for details.


## Contact

Your Name - [Ajaychary Kandukuri](https://www.linkedin.com/in/ajaychary-kandukuri-053a5a25a) - ajaycharykandukuri0629@gmail.com
