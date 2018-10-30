import tensorflow

class LSTM:

    def __init__(self, sample_size, n_hidden):
        self.sample_size = sample_size
        self.n_hidden = n_hidden

        self. weights = {
            'out': tf.Variable(tf.random_normal([n_hidden, sample_size]))
        }

        self. biases = {
            'out': tf.Variable(tf.random_normal([sample_size]))
        }

# above is class outline, below im still working through some stuff

def RNN(x, weights, biases):

   # reshape to [1, n_input]
   x = tf.reshape(x, [-1, n_input])

   # Generate a n_input-element sequence of inputs
   # (eg. [had] [a] [general] -> [20] [6] [33])
   x = tf.split(x,n_input,1)

   # 1-layer LSTM with n_hidden units.
   rnn_cell = rnn.BasicLSTMCell(n_hidden)

   # generate prediction
   outputs, states = rnn.static_rnn(rnn_cell, x, dtype=tf.float32)

   # there are n_input outputs but
   # we only want the last output
   return tf.matmul(outputs[-1], weights['out']) + biases['out']
