from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm


def evaluate(y_tr, tr_preds, y_te, te_preds):
    """
    Evaluates the  R2, RMSE, and MAE scores of a model.

    :param y_tr: Values for 'price' in training dataset
    :param tr_preds: Predicted values for 'price' in training dataset
    :param y_te:  Values for 'price' in training dataset
    :param te_preds: Predicted values for 'price' in test dataset
    :return: None
    """
    print(f"Train R2: {r2_score(y_tr, tr_preds):.4f}")
    print(f"Test R2: {r2_score(y_te, te_preds):.4f}")
    print("****")
    print(f"Train RMSE: ${mean_squared_error(y_tr, tr_preds, squared=False):,.2f}")
    print(f"Test RMSE: ${mean_squared_error(y_te, te_preds, squared=False):,.2f}")
    print("****")
    print(f"Train MAE: ${mean_absolute_error(y_tr, tr_preds):,.2f}")
    print(f"Test MAE: ${mean_absolute_error(y_te, te_preds):,.2f}")


def check_assumptions(X_train, y_train, train_preds, test_preds, y_test):
    """
    Creates graphs to assist in checking the assumptions of linearity.

    :param X_train: X values of model
    :param y_train: Values for 'price' in training dataset
    :param train_preds: Predicted values for 'price' in training dataset
    :param test_preds: Predicted values for 'price' in test dataset
    :param y_test: Values for 'price' in training dataset
    :return:
    """
    # Check Linearity
    train_df = pd.concat([X_train, y_train], axis=1)
    train_df.corr().price.sort_values(ascending=False)
    sns.pairplot(train_df)
    plt.show()

    # Check Multicollinearity
    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(train_df.corr(), annot=True, )
    plt.show()

    # Check for residual normality
    train_residuals = y_train - train_preds
    sm.qqplot(train_residuals, line='r');
    test_residuals = y_test - test_preds
    sm.qqplot(test_residuals, line='r');

    # Checking heteroskedacity
    plt.scatter(train_preds, train_residuals, label='Train')
    plt.scatter(test_preds, test_residuals, label='Test')

    plt.axhline(y=0, color='red', label='0')
    plt.xlabel('predictions')
    plt.ylabel('residuals')
    plt.legend()
    plt.show()
