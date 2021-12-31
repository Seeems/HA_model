from sklearn.metrics import mean_squared_error
import numpy
import matplotlib.pyplot as plt


def func(data):
    ideal_df = data['ideal']
    test_df = data['test']
    train_df = data['train']

    error_dict = {}
    funciton_dict = {}

    ideal_iterator = 1
    lse = 0
    lse_dict = {}
    while ideal_iterator <= (len(ideal_df.columns)-2):

        train_iterator = 1

        while train_iterator <= (len(train_df.columns)-2):
            print((len(train_df.columns)-2))
            for i in train_df[f'y{train_iterator}']:
                for j in ideal_df[f'y{ideal_iterator}']:
                    lse += (j - i)**2

            lse_dict[f'y{ideal_iterator} & y{train_iterator}'] = lse
            error = mean_squared_error(train_df[f'y{train_iterator}'], ideal_df[f'y{ideal_iterator}'])
            print(f'train: y{train_iterator} and ideal: y{ideal_iterator} = {error}')
            error_dict[f'train: y{train_iterator} and ideal: y{ideal_iterator}'] = error
            funciton_dict[f'y{ideal_iterator}'] = error
            train_iterator += 1
        ideal_iterator += 1

    sorted_dict = {k: v for k, v in sorted(funciton_dict.items(), key=lambda item: item[1])}
    sorted_lse_dict = {k: v for k, v in sorted(lse_dict.items(), key=lambda item: item[1])}
    print(sorted_dict)
        #myline = numpy.linspace(1, 22, 100)

        # plt.scatter(x, y)
        #plt.plot(myline, mymodel(myline))
        #plt.show()



    #     lr.fit(, )
    #        print("Training Set R² Score: {:.2f}".format(lr.score(train_df[['x']], train_df[[f'y{y}']])))
    #
    #  print("Test Set R² Score: {:.2f}".format(lrs[i].score(test_df[['x']], test_df[['y']])))

