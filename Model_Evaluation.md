---
created: 2026-05-20 00:34
modified: 2026-05-20 00:34
area: "Machine Learning"
tipo_nota: captura_rapida
status: 🌱
nivel-comprension: ""
proxima-revision: 2026-05-27
ultima-revision: ""
veces-revisado: 0
tiempo-repaso: ""
cards-deck: ""
tags: [captura_rapida, 2026-05-20]
---

# Model Evaluation

> [!info] Metadata
> **Fecha**: 2026-05-20
> **Área**: Machine Learning

---

## 📝 Desarrollo de la Nota

Model Evaluation is the process of evaluating a model to determine its performance and accuracy.

It consists of three main steps:
1. **Train the model**: Train the model on the training data.
2. **Evaluate the model**: Evaluate the model on the test data.
3. **Tune the model**: Tune the model on the validation data.

## Train Set

Is a set of data used to train the model. Usually is the 70% of the data.

## Test Set

Is a set of data used to evaluate the model. Usually is the 30% of the data.

## Validation Set

Is a set of data used to tune the model. Usually is the 10% of the data.

After training the model, we need to evaluate its performance.

## Metrics

The performance of the model is evaluated using metrics that measure its accuracy, precision, recall, and F1-score.

## Overfitting

Overfitting is a phenomenon in machine learning where a model learns the training data too well, including the noise and outliers, resulting in poor performance on new, unseen data.

## Underfitting

Underfitting is a phenomenon in machine learning where a model learns the training data too poorly, including the noise and outliers, resulting in poor performance on new, unseen data.

## K-Fold Cross Validation

K-Fold Cross Validation is a technique used to evaluate the performance of a model on unseen data. It consists of splitting the data into k folds, where k is a number between 2 and 10. Each fold is used as a test set, and the remaining k-1 folds are used as a training set. The model is trained on the training set and evaluated on the test set. The performance of the model is the average of the performance on all k folds.

This type of validation is more robust than the traditional train-test split because it uses all the data for both training and testing, reducing the bias and variance of the model evaluation.

## Bias and Variance

Both bias and variance can lead to overfitting or underfitting. The goal is to find a model that minimizes both, achieving the best possible performance on unseen data.

## Classification and Regression Metrics

classification metrics: 
    - Accuracy: 
    - Precision: 
    - Recall: 
    - F1-Score: 

regression metrics: 
    - Mean Squared Error (MSE)
    - Root Mean Squared Error (RMSE)

Classification problems metrics

to evaluate a classification model like a image reconition model label data as 'cat' or 'not cat':

Step 1: Send the held-out observations where you know the target values to the model.

Step 2: Compare the predictions returned by the model against the actual target values.

Step 3: Calculate the classification metrics.

These metrics help us understand how well the model performs on unseen data and identify potential issues like overfitting or underfitting. By analyzing these metrics, we can make informed decisions about whether the model is ready for deployment or requires further improvement.

## Confusion Matrix

A confusion matrix is a table that summarizes the performance of a classification model. It shows the number of correct and incorrect predictions made by the model, broken down by class. 

Predictions (from the model)

        Actual (true)           Actual (true)        
        Class A                 Class B     

Predicted (model)     True Positives      False Negatives     
Class A          

Predicted (model)     False Positives     True Negatives
Class B

Where:

    - True Positives: The number of correct predictions for a specific class.
    - True Negatives: The number of correct predictions for the other class.
    - False Positives: The number of incorrect predictions for a specific class (the model predicted this class, but it was actually the other class).
    - False Negatives: The number of incorrect predictions for the other class (the model predicted the other class, but it was actually this class).

## Accuracy

Accuracy is the ratio of the number of correct predictions to the total number of predictions. It is calculated as:

Accuracy = (True Positives + True Negatives) / (True Positives + True Negatives + False Positives + False Negatives)

## Precision

Precision is the ratio of the number of correct positive predictions to the total number of positive predictions. It is calculated as:

Precision = True Positives / (True Positives + False Positives)

## Recall

Recall is the ratio of the number of correct positive predictions to the total number of actual positive cases. It is calculated as:

Recall = True Positives / (True Positives + False Negatives)

## F1-Score

F1-Score is the harmonic mean of precision and recall. It is calculated as:

F1-Score = 2 * (Precision * Recall) / (Precision + Recall)

## AUC-ROC Curve

### ROC Curve

ROC is a probability curve that illustrates the diagnostic ability of a binary classifier system as its discrimination threshold varies. The curve is plotted with the True Positive Rate (TPR) on the y-axis and the False Positive Rate (FPR) on the x-axis.

### AUC (Area Under the Curve)
AUC is the area under the ROC curve. It is a measure of the overall performance of the model. The AUC value ranges from 0 to 1, where 1 is the best possible performance and 0 is the worst possible performance.

## Regression problems metrics

For regression problems, we can use the following metrics: 
- MSE (Mean Squared Error)
- RMSE (Root Mean Squared Error)

## Business metrics 

Business metrics are metrics that are used to evaluate the performance of a model in the context of a specific business problem. They measure the impact of the model on the business, such as the increase in revenue or the decrease in costs.

