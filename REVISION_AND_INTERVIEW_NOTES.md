# Revision Notes and Interview Questions

## Project Overview
- This project is an end-to-end machine learning pipeline for predicting student exam performance.
- The main targets are preprocessing features and training regression models to predict `math_score`.
- Data is loaded from `src/notebook/data/stud.csv` and split into train/test artifacts.
- The preprocessing pipeline is saved as `artifacts/preprocessor.pkl` and the final model as `artifacts/model.pkl`.

## Key Components

### `src/components/data_ingestion.py`
- Reads raw CSV data.
- Creates `artifacts/train.csv`, `artifacts/test.csv`, and `artifacts/data.csv`.
- Uses `train_test_split` from scikit-learn.
- Uses `DataIngestionConfig` to define artifact paths.

### `src/components/data_transformation.py`
- Builds the preprocessing pipeline with `Pipeline` and `ColumnTransformer`.
- Applies median imputation and scaling for numerical values.
- Applies most frequent imputation, one-hot encoding, and scaling for categorical values.
- Saves the transformer object with `save_object()`.
- Returns transformed train and test numpy arrays.

### `src/components/model_trainer.py`
- Defines and compares multiple regression models.
- Performs hyperparameter search using `GridSearchCV`.
- Selects the best model by test score.
- Saves the best model object with `save_object()`.

### `src/utils.py`
- Implements `save_object()` and `load_object()` for pickle persistence.
- Implements `evaluate_models()` for training and scoring models.

### `src/exception.py` and `src/logger.py`
- `CustomException` wraps exceptions with contextual traceback information.
- Logging is configured to record important pipeline steps and errors.

## Technical Concepts to Remember
- `ColumnTransformer` allows different preprocessing for numerical and categorical features.
- `Pipeline` chains preprocessing steps and keeps transformations reproducible.
- `train_test_split` prevents data leakage and evaluates generalization.
- `pickle` serializes Python objects for later reuse.
- Custom exceptions improve debugging and maintainability.
- `GridSearchCV` is used for hyperparameter tuning across model candidates.

## Revision Checklist
- Understand the data schema and target variable.
- Know why train/test artifacts are created separately.
- Be able to explain each preprocessing step for numerical vs categorical columns.
- Know the difference between `fit_transform()` and `transform()`.
- Be able to explain why models are evaluated using test data only after training.
- Remember where artifacts are saved and how to load them.
- Know why a generic `python3` kernel may cause environment mismatches in notebooks.

## Common Interview Questions

### 1. What is the purpose of this project?
This project implements a full ML workflow for predicting student math scores based on demographic and academic features. It demonstrates data ingestion, preprocessing, model training, evaluation, and persistence.

### 2. How do you handle categorical and numerical data differently?
Numerical columns are imputed and scaled, while categorical columns are imputed, one-hot encoded, and then scaled. Using a `ColumnTransformer` ensures each feature type receives the appropriate pipeline.

### 3. Why use `Pipeline` and `ColumnTransformer`?
`Pipeline` enforces a consistent sequence of transformations and prevents data leakage. `ColumnTransformer` allows applying different preprocessing steps to different feature groups.

### 4. How does the project save and reuse models?
The project saves preprocessing and model objects using `pickle` via `save_object()` in `src/utils.py`. This allows loading the pipeline and model later without retraining.

### 5. What is a `CustomException` and why is it useful?
`CustomException` wraps original exceptions with additional context, such as file name and line number. It makes debugging easier when errors occur in different pipeline stages.

### 6. Why is `train_test_split` important?
It separates data into training and evaluation sets, enabling a realistic assessment of model generalization and avoiding overfitting to the training data.

### 7. What would you improve next?
- Add validation/cross-validation and a proper model selection pipeline.
- Add unit tests for each component.
- Add an API layer to serve predictions.
- Improve feature engineering and analyze feature importance.
- Use logging and config files for better reproducibility.

### 8. Where would you put the raw dataset in production?
The raw dataset should be stored in a dedicated data directory or data lake; in this repo it is under `src/notebook/data/stud.csv`, but production should use external storage with versioning.

### 9. How would you ensure this project works on any machine?
Use a virtual environment or `requirements.txt`, pin dependencies, and avoid hard-coded working directories. Use absolute paths based on module location when constructing file paths.

### 10. What is the benefit of saving the preprocessor separately from the model?
Saving the preprocessor separately ensures the same preprocessing logic is applied during inference. It also enables reuse of the transformation pipeline even if the model changes.
