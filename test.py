import tensorflow as tf

# Create a variable tensor (mutable)
x = tf.Variable([[1, 2, 3], [4, 5, 6]])

# Create a new tensor with the desired values
new_values = tf.constant([[7, 8, 9], [10, 11, 12], [10, 11, 12]])

# Use the assign method to change the value of x
x.assign(new_values)

# Print the modified tensor
print(x.numpy())
