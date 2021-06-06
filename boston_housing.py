import numpy as np

data_train = np.loadtxt('train.csv', dtype='float', delimiter=',', skiprows=1, usecols=tuple(range(1, 14)))
y = np.loadtxt('train.csv', dtype='float', delimiter=',', skiprows=1, usecols=14, ndmin=2)
data_test = np.loadtxt('test.csv', dtype='float', delimiter=',', skiprows=1, usecols=tuple(range(1, 14)))

data_test = np.concatenate((data_test, np.ones((105, 1))), axis=1)
data_train = np.concatenate((data_train, np.ones((400, 1))), axis=1)

for i in range(0, 13):
    col_max = max(data_train[:, i])
    col_min = min(data_train[:, i])
    data_train[:, i] = (data_train[:, i] - col_min) / (col_max - col_min)
    data_test[:, i] = (data_test[:, i] - col_min) / (col_max - col_min)

y = np.log(y)

def cost_fn(p, data_train, w):
    if p == 2:
        cost = (2 * (np.dot(np.dot(np.transpose(data_train), data_train), w) - np.dot(np.transpose(data_train), y)) + l * p * np.power(np.absolute(w), (p - 1)))
    if p < 2 and p > 1:
        cost = (2 * (np.dot(np.dot(np.transpose(data_train), data_train), w) - np.dot(np.transpose(data_train), y)) + l * p * np.power(np.absolute(w), (p - 1)) * np.sign(w))
    return cost

filenames = {'ridgeRegression_Output.csv': 2.0,
             'p=1.75_Output.csv': 1.75,
             'p=1.5_Output.csv': 1.5,
             'p=1.3_Output.csv': 1.3
             }

for (fname, p) in filenames.items():

    w = np.zeros((14, 1))

    l = 0.2

    t = 0.00012

    w_new = w - t * cost_fn(p, data_train, w)

    i = 0

    while(np.linalg.norm(w_new-w) > 10 ** -10):
        w = w_new
        w_new = w - t * cost_fn(p, data_train, w)
        i = i + 1

    pred_id = np.loadtxt('test.csv', dtype='int', delimiter=',', skiprows=1, usecols=0, ndmin=2)

    y_test = np.exp(np.dot(data_test, w_new))

    np.savetxt(fname, np.concatenate((pred_id, y_test), axis=1), delimiter=',', fmt=['%d', '%f'], header='ID,MEDV', comments='')

