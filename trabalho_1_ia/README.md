# Project 1

## 1. Linear Regression:

A possible set of values ​​that converged to a minimum MSE (high-quality regression) was: {**b = 0, w = 0.1, alpha = 0.91, num_iterations = 100**}

This resulted in a final MSE of 0.014802014531904436. Any changes to these values ​​either resulted in a larger MSE or did not significantly reduce the MSE value (we considered a significant change to be a change of up to 3 decimal places).

It is important to note that the results assume that the features (data) were normalized to the range [0, 1], following the formula: x(i) = (x(i) - min(x)) / (max(x) - min(x)).

During testing, we noticed that the most significant parameter for achieving a good linear regression result was alpha, where small variations, both upward and downward, resulted in a drastic increase in the MSE value. (This implies that with even slightly lower values, the regression couldn't converge quickly enough, and that with slightly higher values, it ended up diverging.) Num_iterations was a distant second, since, at low values, the MSE value explodes quickly but stabilizes at a minimum after just over 30 iterations. The initial values ​​of b and w had almost no impact on the regression quality, implying that the linear regression algorithm is indeed very effective at finding good values ​​for these parameters considering the dataset to which they were applied, regardless of their initial values.

## 2. TensorFlow/Keras:

(Note 1: All values ​​found assume that pixel values ​​were normalized using the formula: pixel_value = pixel_value / 255)

(Note 2: The default model parameters were: 1 layer of neurons with 64 neurons and 32 filters. Other parameters besides the number of layers, neurons in a single layer, and the number of filters were not changed.)

### MNIST:

A dataset of 70,000 images of handwritten numbers (0 to 9). It has 10 classes (the digits 0 to 9), 10,000 training images (out of 70,000), and the images are 784 pixels in size (28 pixels wide * 28 pixels high) and 784 bytes (28 pixels wide * 28 pixels high * 1 color channel).

It is the simplest dataset for the following reasons: 1. The images are monochromatic, so they have fewer attributes to be analyzed to classify each image, reducing the model's complexity. 2. Classes are a subset of "objects" that have similar attribute types (basically circles and vertical and horizontal lines), which also reduces the model's complexity. 3. The attribute values ​​that differentiate one digit from another are relatively easy to identify, which increases the model's accuracy.

The highest accuracy with this dataset was 98.71%, achieved using a 2-layer model (64, 32). However, the relative increase in accuracy was largely insignificant, since the accuracy using a 1-layer model (64) was 98.50%, while the time increase almost doubled (65.50s -> 125.15s). Other parameters that, when changed, increased accuracy, but with less significance, were: a 1-layer model with more neurons (512), a 2-layer model (32, 64), and a model with fewer filters (16). Models with fewer neurons (8) and more filters reduced accuracy.

### Fashion MNIST:

A dataset of 70,000 clothing images. It has 10 classes (T-shirt, Trouser, Pullover, Dress, Coat, Sandal, Shirt, Sneaker, Bag, Ankle Boot), 10,000 training images (out of 70,000), and the images are 784 pixels in size (28 pixels wide * 28 pixels high) and 784 bytes (28 pixels wide * 28 pixels high * 1 color channel).

It is relatively more complex than MNIST, but still quite simple. The additional complexity arises from the fact that there are many more attributes/features to be identified in the images, coupled with the fact that some instances are difficult to classify between two classes that end up having very similar attribute types (e.g., T-shirt and Shirt). However, the relative similarity between some classes ends up reducing the total number of features to be learned by the model, which prevents the complexity from increasing too much.

The highest accuracy achieved was 91.48%, achieved by the model with the most filters (64). This result represents a small improvement over the standard model (91.28%), but at a considerably higher training cost (115.69s versus 66.95s). Other changes, such as adding a second layer of neurons or increasing their number, did not yield significant gains in accuracy, remaining around 90.8% and 91.2%. The only change that degraded performance was the drastic reduction of neurons to 8, which decreased accuracy to 87.68%. This suggests that the standard architecture is already quite effective for this dataset, and very small improvements require a disproportionate increase in computational cost.

### CIFAR-10:

A dataset of 60,000 color images. It has 10 classes (airplane, automobile, bird, cat, deer, dog, frog, horse, ship, truck), 10,000 training images (out of 60,000), and the images are 1024 pixels in size (32 pixels wide * 32 pixels high) and 3072 bytes (32 pixels wide * 32 pixels high * 3 color channels).

It is significantly more complex than the previous two datasets. This is primarily due to the addition of two color channels, which add many features to be identified in each image. Furthermore, because the classes are very different from each other, the total number of features to be identified increases even further, and consequently, the complexity as well.

For this dataset, the highest accuracy was 65.27%, achieved using a model with more filters (64). This was a notable improvement compared to the default model (63.48%), although the training time almost doubled (132.25s vs. 72.64s). Increasing the number of neurons to 512 also resulted in good accuracy (64.86%), but with an excessively high training time (332.21s), proving to be an inefficient tradeoff. On the other hand, reducing the number of neurons (8) or inappropriately adding a second layer (32, 64) led to a sharp drop in performance. The results indicate that, for the complexity of CIFAR-10 color images, increasing the model's ability to learn features (more filters) is more effective than simply adding more layers or neurons in the tested configuration.

### CIFAR-100:

A dataset of 60,000 color images. It has 100 classes, separated into 20 superclasses (aquatic mammals, fish, flowers, food containers, fruits and vegetables, household electrical devices, household furniture, insects, large carnivores, large man-made outdoor objects, large natural outdoor scenes, large omnivores and herbivores, medium-sized mammals, non-insect invertebrates, people, reptiles, small mammals, trees, vehicles 1, vehicles 2). 10,000 images for training (out of 60,000), and the images are 1024 pixels in size (32 pixels wide * 32 pixels high) and 3072 bytes (32 pixels wide * 32 pixels high * 3 color channels).

This is by far the most complex dataset. This is due to the very high number of classes into which the images can be classified. Due to the extremely high number, this dataset simultaneously has a very high total number of features to be identified, and difficulty classifying some images into two relatively similar classes (e.g., aquatic mammals vs. fish). In other words, the existence of similar classes does not result in a smaller number of features to be learned because of the high total number of classes. Furthermore, the images are also in color.

The best accuracy result, 32.79%, was achieved with the model that used the most neurons (512) in the dense layer. This was the most significant gain among all tests, outperforming the standard model (29.79%) by 3 percentage points, but at the cost of the longest training time recorded (334.69s). Interestingly, the second best result (30.86%) was obtained with the model with the fewest filters (16), which was also one of the fastest (41.22s). This contrasting behavior suggests that, for the high complexity of CIFAR-100, two strategies may be viable: a larger network in the final layer to better separate the 100 classes, or a smaller network in the filters to avoid overfitting, given the low number of samples per class. Adding a second layer of neurons proved detrimental, drastically reducing accuracy.

### Results Table: accuracy/time

| Parameters/Models | CIFAR-10 | Fashion MNIST | MNIST | CIFAR-100 |
|-------------------|-------------------|-------------------|-------------------|-------------------|
| Standard (filters=32, kernel_size=(3,3), activation='relu', pool_size=(2,2), dense_units=64, optimizer='adam') | 63.48%, 72.64s | 91.28%, 66.95s | 98.50%, 65.50s | 29.79%, 69.07s |
| 2 layers (64, 32) | 63.89%, 146.18s | 90.86%, 119.42s | 98.71%, 125.15s | 22.21%, 135.37s |
| 2 layers (32, 64) | 57.17%, 97.95s | 90.94%, 89.58s | 98.50%, 90.46s | 27.52%, 105.16s |
| more neurons (512) | 64.86%, 332.21s | 90.83%, 304.48s | 98.59%, 301.87s | 32.79%, 334.69s |
| less neurons (8) | 10.00%, 45.50s | 87.68%, 43.43s | 97.34%, 46.94s | 1.00%, 46.66s |
| more filters (64) | 65.27%, 132.25s | 91.48%, 115.69s | 98.28%, 117.01s | 26.92%, 135.48s |
| less filters (16) | 61.18%, 40.28s | 90.87%, 40.98s | 98.52%, 39.55s | 30.86%, 41.22s |
