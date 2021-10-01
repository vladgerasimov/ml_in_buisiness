# Handwritten digits recognition

#### The app uses the neural network of following structure to predict a digit between 0 and 9

![image](nn_structure.png)

#### The app receives a set of n images of 28x28 pixels as a matrix of shape (n x 784)

#### Clone repository and build an image of a docker container:
```sh
git clone https://github.com/vladgerasimov/ml_in_buisiness.git
cd ml_in_buisiness
docker build -t digits_net .
```
#### Run container:
```sh
docker run -d -p 8181:8181 -v app/models:/app/app/models digits_net
```



