## Student Information
**Name:** Khoa Doan
**Date:** 05/03/2026
**Algorithm Analysis:** K-Nearest Neighbors (KNN) Regression for Bakery Loaf Prediction

---

## Algorithm Understanding

**What type of problem is this algorithm solving?**\
Supervised learning regression — predicting a continuous numerical output (loaves) from labeled historical data.

**How does KNN regression differ from KNN classification?**\
Classification votes among neighbors to assign a category; regression averages neighbors' values to produce a number.

**What does the "K" in KNN represent, and why did we choose k=4 for this problem?**\
K is the number of nearest neighbors to consult. k=4 balances specificity and generalization for a 20-point dataset.

**In your own words, explain how the model produces a prediction for a new day.**\
It finds the 4 historical days most similar to today's conditions and averages their loaf counts.

---

## Implementation Questions

**Why do we separate the DataFrame into features (X) and target (y) before training?**\
The model needs to know what to learn from (X) versus what to predict (y). Scikit-learn requires them as separate inputs.

**Why must the input to `model.predict()` be a 2D array (e.g., `[[4, 1, 0]]`) instead of a 1D array (`[4, 1, 0]`)?**\
Scikit-learn expects a batch of samples where rows=samples and columns=features. A 1D array is ambiguous

**What does `.fit(X, y)` actually do for a KNN model? (Hint: it's different from most other ML algorithms.)**\
It just stores the training data. KNN does no computation during training — all work happens at prediction time.

**Why do we use `.values` when extracting columns from the DataFrame?**\
It converts pandas objects to numpy arrays, which is what scikit-learn expects.

---

## Extension: Choosing K

**What would happen if we set k=1? What are the risks?**\
The model copies the single closest point — overfitting, highly sensitive to noise.

**What would happen if we set k=20 (the size of the entire dataset)? What does the model become?**\
Every prediction becomes the global average, completely ignoring today's conditions.

**How would you decide what value of k is best for a given dataset?**\
Cross-validation — test multiple k values and pick the one with the lowest validation error.

---

## Extension: Distance and Feature Scaling

**KNN uses distance to find "nearest" neighbors. Our features have very different ranges: weather is 1–5, but weekend_holiday and game_on are 0/1. Why could this be a problem?**\
Weather differences contribute more to distance than binary features, causing weather to unfairly dominate neighbor selection.

**Give an example of two days where the weather feature would unfairly dominate the distance calculation.**\
[Day A (weather=1, weekend=1, game=1) vs Day B (weather=5, weekend=1, game=1): distance is 4, entirely from weather despite identical binary features.]

**How would you modify the data preparation step to fix this? (Hint: look up "feature scaling" or "StandardScaler".)**\
Apply StandardScaler to normalize all features to mean=0, std=1 before training.

---

## Reflection Questions

**What is a limitation of KNN regression? Provide a scenario where it would make a poor prediction.**\
It can't extrapolate beyond training data. A day with a completely unseen combination of conditions will get poor neighbors and an inaccurate prediction.

**Our dataset only has 20 days of data. How might the predictions change if we had 2,000 days of data instead?**\
Neighbors would be much closer matches to today's conditions, making predictions more accurate and stable.

**What other features (beyond weather, weekend/holiday, and game day) could the bakery collect to improve predictions?**\
Day of week, season, temperature, local events, school holidays, nearby competitor hours.

**KNN is sometimes called a "lazy learning" algorithm because it does almost no work during training. What is the tradeoff at prediction time?**\
Every prediction requires comparing against all training points, making it slower as the dataset grows.

**The autograder expects a prediction of approximately 70.5 loaves for today's conditions. Manually look at the dataset and identify which 4 historical days you think the model is averaging. Do their loaf counts average to 70.5?**\
Days with (weather=4, weekend=1, game=0) loaves=72 and 75, plus two nearby neighbors. Their average lands near 70.5.

**Why might a bakery prefer a slightly inaccurate ML prediction over a human guess for daily loaf counts?**\
ML is consistent, unbiased, and improves with more data — human guesses are inconsistent and don't scale.

**If the bakery wanted to MINIMIZE waste (unsold loaves) rather than just predict accurately, how might you change the approach?**\
Predict a lower percentile of neighbor values, or use an asymmetric loss function that penalizes overproduction more than underproduction.s
