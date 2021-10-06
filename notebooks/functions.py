#<<<<<<< HEAD

#=======
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error

def evaluate(y_tr, tr_preds, y_te, te_preds):
    """

    :param y_tr: Values for 'price' in training dataset
    :param tr_preds: Predicted values for 'price' in training dataset
    :param y_te: Values for 'price' in test dataset
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
#>>>>>>> main
