# Project 1

## 1. Linear Regression:

A possible set of values ​​that converged to a minimum MSE (high-quality regression) was:

b = 0
w = 0.1
alpha = 0.91
num_iterations = 100

This resulted in a final MSE of 0.014802014531904436. Any changes to these values ​​either resulted in a larger MSE or did not significantly reduce the MSE value (we considered a significant change to be a change of up to 3 decimal places).

It is important to note that the results assume that the features (data) were normalized to the range [0, 1], following the formula: x(i) = (x(i) - min(x)) / (max(x) - min(x)).

During testing, we noticed that the most significant parameter for achieving a good linear regression result was alpha, where small variations, both upward and downward, resulted in a drastic increase in the MSE value. (This implies that with even slightly lower values, the regression couldn't converge quickly enough, and that with slightly higher values, it ended up diverging.) Num_iterations was a distant second, since, at low values, the MSE value explodes quickly but stabilizes at a minimum after just over 30 iterations. The initial values ​​of b and w had almost no impact on the regression quality, implying that the linear regression algorithm is indeed very effective at finding good values ​​for these parameters considering the dataset to which they were applied, regardless of their initial values.

## 2. TensorFlow/Keras:

(Note 1: All values ​​found assume that pixel values ​​were normalized using the formula: pixel_value = pixel_value / 255)

(Note 2: The default model parameters were: 1 layer of neurons with 64 neurons and 32 filters. Other parameters besides the number of layers, neurons in a single layer, and the number of filters were not changed.)

### MNIST:

A dataset of 70,000 images of handwritten numbers (0 to 9). It has 10 classes (the digits 0 to 9), 10,000 training images (out of 70,000), and the images are 784 pixels in size (28 pixels wide * 28 pixels high) and 784 bytes (28 pixels wide * 28 pixels high * 1 color channel).

It is the simplest dataset for the following reasons: 1. The images are monochromatic, so they have fewer attributes to be analyzed to classify each image, reducing the model's complexity. 2. Classes are a subset of "objects" that have similar attribute types (basically circles and vertical and horizontal lines), which also reduces the model's complexity. 3. The attribute values ​​that differentiate one digit from another are relatively easy to identify, which increases the model's accuracy.
