# Homework 5

1. TensorFlow is a library for deep learning.  Google is the leading contributor.
2. TensorRT sits on top of TensorFlow and optimizes for GPU systems.
3. ImageNet is a large repository of labeled images for training.  It has over 15 million labled images across over 22,000 classes.
4. GoogleNet significantly reduced the number of operations compared to its predecessors by using 1X1 convolutions prior to applying larger filters.  This worked by essentially reducing the input size to the larger convolution by performing a cheaper operation first.  MobileNet further decreases the computational cost by segregating the number of channels within each layer from each other.  Each filter no longer has to do multiplications at every channel.
5. A bottleneck layer has fewer features than its previous layers and is useful as compression method for the input (e.g. the middle layer in an autoencoder).
6. A cached bottleneck for an input is just a compressed representation that can be reused.  Layer freezing means not allowing backpropagation to change the values in a layer and is independent of input.
7. The lab used the frozen layers to compute cached bottlenecks for each input image.  This way, they did not have to be recomputed for each epoch.
8. Lower learning rate increases the precision, but training takes much longer.
9. Higher learning rate decreases training time, but the network ends up overshooting minima and precision suffers.
10. The model was pretty good.
11. GPU vs CPU training time on MobileNet is actually fairly comparable.
12. Inception takes way longer to train on CPU than on GPU.
13. 
```bash
python3 -m scripts.label_image --input_layer="Mul" --input_height=299 --input_width=299  --graph=tf_files/retrained_graph.pb --image=tf_files/flower_photos/daisy/21652746_cc379e0eea_m.jpg
```
