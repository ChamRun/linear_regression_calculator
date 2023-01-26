import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def main():
    # We want to read the csv file.
    # It has no headers and the first line is the data.
    # The first column is x and the second column is y.

    df = pd.read_csv('data.csv', header=None, names=['x', 'y'])

    train_percent = 0.95
    train_size = int(train_percent * len(df))

    train_df = df.iloc[:train_size]
    test_df = df.iloc[train_size:]

    a, b = find_a_b_based_on_least_squares(train_df)
    test_result = test_a_b(a, b, test_df)

    for i in range(len(test_result)):
        print(f'Read value: {test_result[i][0]}'
              f'\nEstimated value: {test_result[i][1]}'
              f'\nError: {test_result[i][2]}\n')

    plt.plot(df['x'], df['y'], 'o')
    plt.plot(df['x'], a * df['x'] + b)
    plt.show()


def multiply_dataframes(df1, df2):
    # convert dataframes to numpy matrices
    mat1 = df1.values
    mat2 = df2.values
    # perform matrix multiplication
    result = np.matmul(mat1, mat2)
    # return as a DataFrame
    return pd.DataFrame(result)


def find_a_b_based_on_least_squares(df):
    x = df['x']
    y = df['y']
    n = len(x)
    sum_x = sum(x)
    sum_y = sum(y)
    sum_xy = sum(x * y)
    sum_x_squared = sum(x ** 2)
    a = (n * sum_xy - sum_x * sum_y) / (n * sum_x_squared - sum_x ** 2)
    b = (sum_y - a * sum_x) / n
    return a, b


def test_a_b(a, b, df):
    x = df['x'].values
    y = df['y'].values
    test_result = []
    for i in range(len(x)):
        read_value = y[i]
        estimated_value = a * x[i] + b
        error = abs(read_value - estimated_value)
        test_result.append([read_value, estimated_value, error])

    return test_result


if __name__ == '__main__':
    main()
