# Lab 10: Truck Parking

## Student Information
- **Name:** Khoa Doan
- **Date:** 04/19/2026  


# Algorithm Understanding

**What type of problem is this algorithm solving?**  
This is an optimization/approximation problem — specifically a bin packing problem, which is a classic NP-hard combinatorial optimization challenge. The goal is to fit as many boxes as possible into a truck of fixed volume without exceeding its capacity

**Is this greedy algorithm guaranteed to produce the optimal solution? Why or why not?**  
No. A greedy algorithm makes the locally optimal choice at each step, but this does not guarantee a globally optimal result. For example, one large box might block several medium boxes that together would fill the truck more completely. 

**What is the greedy choice made in this algorithm?**  
The algorithm selects the largest remaining box that still fits within the truck's remaining capacity



# Implementation Questions

**Why do we sort the boxes in descending order of volume before packing?**  
Sorting in descending order ensures we try to place the biggest boxes first. This typically leads to better space utilization because large boxes are harder to fit later once only small gaps remain.

**What would happen if we sorted the boxes in ascending order instead?**  
Small boxes would be packed first, potentially filling up the truck with many tiny boxes while leaving no room for larger ones. This would generally result in fewer total volume units packed and a worse overall solution.

**Why do we keep track of `used_volume`?**  
used_volume acts as a running total of how much of the truck's capacity has been consumed. It allows us to check, before adding each new box, whether that box would push us over the truck's volume limit. Without it, we'd have no way to enforce the capacity constraint.



# Extension: Dimension Constraints

**Why is checking only volume not sufficient for real-world packing?**  
Volume alone treats a box as a flexible blob of space, but physical boxes have fixed shapes. A box might have a smaller volume than the truck's remaining space yet still be too long, wide, or tall to fit  within its interior dimensions.

**Give an example where a box fits by volume but not by dimensions.**  
Truck dimensions: 4 x 4 x 4 (volume = 64 cubic units). Remaining capacity: 30 cubic units.
Box: 10 x 1 x 2 (volume = 20 cubic units — fits by volume).
However, the box is 10 units long and the truck is only 4 units in every dimension, so the box physically cannot fit inside.

**How would you modify the algorithm to check dimension constraints before packing a box?**  
Add a dimension check inside the loop before appending a box to packed_boxes. Since boxes can be rotated, we'd check all axis permutations of the box against the truck dimensions:



# Reflection Questions

**What is a limitation of this greedy approach? Provide a scenario where it fails to find the optimal solution.**  
The greedy approach can miss combinations of smaller boxes that collectively fill the truck better. Example: Truck volume = 10. Boxes have volumes [6, 5, 5]. The greedy algorithm picks the box of volume 6 first (used = 6), then finds neither 5-unit box fits (6 + 5 = 11 > 10). It packs only 6 units. The optimal solution would be the two 5-unit boxes, packing 10 units total.

**How is this problem related to the Knapsack Problem?**  
Both problems require making choices that adhere to constraints (weight for Knapsack, volume for Truck Packing) and aim to maximize a specific goal (value for Knapsack, space utilization for Truck Packing).

**What type of algorithm would guarantee an optimal solution for this problem? What is the tradeoff?**  
A dynamic programming (DP) or exhaustive brute-force search would guarantee the optimal solution by evaluating all possible subsets of boxes. The tradeoff is time complexity

**If the truck had weight limits in addition to volume, how would the algorithm need to change?**  
Each Box would need a weight attribute. The packing condition would expand to check both constraints simultaneously. The sorting would also become more nuanced — we might sort by a combined efficiency metric (volume-to-weight ratio) rather than volume alone.

**Why are greedy algorithms often preferred despite not always being optimal?**  
Greedy algorithms are fast (often O(n log n)) and simple to implement and understand. For many practical problems — especially large-scale ones — finding a near-optimal solution quickly is far more valuable than waiting a prohibitively long time for the perfect answer. 
