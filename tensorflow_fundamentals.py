import tensorflow as tf

# print(tf.__version__)


# Create tensors
scalar = tf.constant(7)
# print(scalar)

# Check the number of dimensions of a tensor
# print(scalar.ndim)

# Create a vector
vector = tf.constant([10,10])
# print(vector)

# Check the dimension of vector
# print(vector.ndim)


# Create a Matrix
matrix = tf.constant([[10,7],
                     [7,10]])
# print(matrix)

# Check the dimensions
# print(matrix.ndim)

# Create another matrix
another_matrix = tf.constant([[10.,7.],
                              [8.,9.],
                              [3.,7,]],dtype=tf.float16)
# print(another_matrix)
# print(another_matrix.ndim)

# Create a tensor
tensor = tf.constant([[[1,2,3],
                       [4,5,6,]],
                      [[7,8,9],
                       [10,11,12]],
                      [[13,14,15],
                       [16,17,18]]])
# print(tensor)
# print(tensor.ndim)


### Creating Tensors with tf.Variable

# create the same tensor
changeable_tensor = tf.Variable([10,7])
unchangeable_tensor = tf.constant([10,7])

# print(changeable_tensor)
# print(unchangeable_tensor)

# Changing an element
changeable_tensor[0].assign(11)
# unchangeable_tensor[0].assign(11)

# print(changeable_tensor)
# print(unchangeable_tensor)

### Creating Random Tensors

random_1 = tf.random.Generator.from_seed(42)
random_1 = random_1.normal(shape=(3,2))
print(random_1)
