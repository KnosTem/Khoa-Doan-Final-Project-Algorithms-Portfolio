# Chapter 12: KNN Regression — Lab Report

## Student Information
- **Name:** Khoa Doan
- **Date:** 05/03/2026
- **Course:** COSC 2436

---

## Algorithm Summary
- **How it works:** K-Nearest Neighbors regression finds the k most similar historical data points to a new input and averages their target values to produce a prediction. For each new day, the model measures the distance between today's conditions and every historical day, selects the 4 closest matches, and returns their average loaf count as the forecast.
- **Time complexity:** O(n × d) per prediction, where n is the number of training points and d is the number of features. Training is O(1) since KNN simply stores the data.
- **When to use it:** Best suited for small-to-medium datasets where the relationship between features and target is local and non-linear. Works well when similar inputs reliably produce similar outputs, such as demand forecasting based on recurring conditions.

---

## Test Results

**Program output:**

```
Features shape: (20, 3)
Target shape: (20,)

KNN model trained with k=4

Today's conditions: Weather=4, Weekend/Holiday=1, Game=0
Predicted loaves to bake: 70.5
```

**Prediction breakdown — identifying the 4 nearest neighbors:**

| Day | Weather | Weekend/Holiday | Game | Loaves |
|-----|---------|-----------------|------|--------|
| 4   | 4       | 1               | 0    | 72     |
| 20  | 4       | 1               | 0    | 75     |
| 15  | 5       | 0               | 1    | 70     |
| 19  | 2       | 1               | 1    | 70     |

Average: (72 + 75 + 70 + 70) / 4 = **70.5** ✓

---

## Reflection Questions

1. **What does `.fit(X, y)` actually do for a KNN model, and how is it different from most other ML algorithms?**  
   For KNN, `.fit()` simply stores the training data — it performs no computation or parameter updates. Most algorithms (like linear regression or neural networks) use training time to learn weights or decision boundaries. KNN is a "lazy learner" that defers all computation until prediction time, when it must compare the new input against every stored point.

2. **What would happen if we set k=1, and what would happen if we set k=20?**  
   With k=1 the model copies the single closest historical day exactly, which leads to overfitting and high sensitivity to noise or outliers. With k=20 every prediction becomes the global average of all loaf counts regardless of today's conditions, making the model too rigid to respond to any meaningful variation in weather or day type.

3. **Why could the difference in feature ranges (weather 1–5 vs. binary 0/1) be a problem for KNN, and how would you fix it?**  
   KNN calculates distance across all features equally, so weather differences (up to 4 units apart) will dominate over binary features that can only differ by 1. For example, two days that share the same weekend and game status but differ by 4 in weather will appear much "farther apart" than two days with opposite weekend status but similar weather, even if the weekend matters more. Applying `StandardScaler` to normalize all features to the same range before training would fix this.

---

## Challenges Encountered

The trickiest part was understanding why `model.predict()` requires a 2D array even for a single day. Passing `[4, 1, 0]` directly raises a shape error because scikit-learn always expects rows of samples — a 1D array is ambiguous. Wrapping the input in double brackets as `np.array([[4, 1, 0]])` resolved it. Manually verifying the 70.5 prediction by cross-referencing the dataset to find the likely 4 nearest neighbors also helped build intuition for how the distance calculation actually selects neighbors.
