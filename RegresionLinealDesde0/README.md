# Linear Regression from Scratch in Python

This project demonstrates how to implement a simple **linear regression model** from scratch using **NumPy**, including:

* Synthetic data generation
* Parameter initialization
* Prediction function
* Gradient Descent optimization
* Evaluation metrics (MSE and R²)

The goal is to provide an educational and practical example of how linear regression works internally, without relying on high‑level machine learning libraries.

---

## 📘 Project Overview

Linear regression is one of the foundational algorithms in machine learning. It models the relationship between a dependent variable and one or more independent variables by fitting a linear equation.

This project walks through all the essential components:

1. **Data Generation** – Creating synthetic linear data with noise.
2. **Feature Preparation** – Adding a bias term to the feature matrix.
3. **Gradient Descent** – Optimizing model parameters.
4. **Predictions** – Applying the model to estimate outputs.
5. **Evaluation** – Measuring model performance.

---

## 📊 Mathematical Background

Given training data:

* Feature matrix: **X**
* Target vector: **y**
* Parameters (weights): **θ**

### Hypothesis Function

The model predicts values using:

```
h_θ(x) = X · θ
```

### Cost Function: Mean Squared Error (MSE)

```
J(θ) = 1/m * Σ (h_θ(xᵢ) - yᵢ)²
```

### Gradient Descent Update Rule

```
θ := θ − α * (2/m) * Xᵀ·(X·θ − y)
```

Where:

* α is the learning rate
* m is the number of samples

---

## 🧪 Code Structure

The main components of the script are:

### 1. Data Generation

Synthetic dataset following the equation:

```
y = 4 + 3X + noise
```

### 2. Gradient Descent Implementation

Iteratively updates parameters to minimize the error.

### 3. Metrics

* **MSE (Mean Squared Error)** to measure average squared error.
* **R² Score** to evaluate model accuracy.

### 4. Output

The script prints:

* Optimized parameters (θ₀ and θ₁)
* MSE value
* R² score

---

## ▶️ How to Run

1. Ensure you have Python installed.
2. Install NumPy:

```
pip install numpy
```

3. Run the script:

```
python linear_regression.py
```

---

## 📈 Example Output

You will see something like:

```
Optimized parameters (Theta): [[4.02], [2.98]]
MSE: 1.03
R2: 0.95
```

Values may vary slightly due to random initialization.

---

## 🎯 Purpose

This project is ideal for students and developers who want to understand:

* How linear regression works under the hood
* Gradient descent mechanics
* Basic model evaluation techniques

It serves as a foundation for studying more advanced machine learning algorithms.

---

## 📚 License

This project is for educational purposes and is freely usable and modifiable.

---

Feel free to extend the model with:

* Polynomial features
* Regularization (Ridge/Lasso)
* Mini‑batch or stochastic gradient descent

Happy coding!
