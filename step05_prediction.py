from tensorflow.keras.models import load_model
import matplotlib.pyplot as plt
import numpy as np


if __name__ == '__main__':
    _, x_test, _, y_test = np.load('./training_metadata.npy', allow_pickle=True)
    model = load_model('./test_model.h5')
    predict = model.predict(x_test)

    actual_dict = {'avg_tmp': [], 'min_tmp': [], 'max_tmp': []}
    predict_dict = {'avg_tmp': [], 'min_tmp': [], 'max_tmp': []}
    error_dict = {'avg_tmp': [], 'min_tmp': [], 'max_tmp': []}
    for i in range(len(predict)):
        for idx, key in enumerate(actual_dict):
            actual_dict[key].append(y_test[i][idx])
            predict_dict[key].append(predict[i][idx])
            error_dict[key].append(y_test[i][idx] - predict[i][idx])

    # print(actual_dict['avg_tmp'][:3])
    # print(predict_dict['avg_tmp'][:3])

    plt.plot(actual_dict['avg_tmp'][:100], label='actual_avg_tmp')
    plt.plot(predict_dict['avg_tmp'][:100], label='predict_avg_tmp')
    plt.plot(error_dict['avg_tmp'][:100], label='error_ratio')
    plt.legend()
    plt.show()
