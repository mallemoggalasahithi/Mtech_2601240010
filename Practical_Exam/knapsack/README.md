Q) A cloud service provider has a limited amount of computing resources. Each application requires a specific amount of resources and generates a certain revenue. Each application can either be deployed completely or not deployed. 
Task: Implement the 0/1 Knapsack Dynamic Programming algorithm to maximize revenue within the available resource capacity. 
The program must display: 
- Maximum revenue. 
- Selected applications. 
- DP table. 
- Time complexity. 
- Space complexity.

ANSWER:
----------
0/1 Knapsack for Cloud Applications

(1) AIM:
To select cloud applications within a limited resource capacity and maximize total revenue using the 0/1 Knapsack dynamic programming algorithm.

(2) DESCRIPTION:
Each cloud application consumes computing resources and produces a certain revenue. Each application is either fully deployed or not deployed at all. Dynamic programming is used to find the optimal combination that yields the maximum revenue without exceeding the maximum resource capacity.

(3) ALGORITHM:
1) Read $N$ cloud applications.
2) Read resource requirements and revenue for each application.
3) Read the maximum cloud resource capacity $W$.
4) Create a DP table with $N+1$ rows and $W+1$ columns.
5) Initialize zero-resource cases to zero.
6) For each application and capacity, check whether it fits.
7) If it fits, calculate include and exclude revenue.
8) Store the larger value in the DP table.
9) Backtrack to find the selected applications.
10) Display maximum revenue, selected applications, DP table, time complexity, and space complexity.

(4) SAMPLE OUTPUT:

Maximum revenue: 7

Selected applications: [1, 2]

DP Table:
[0, 0, 0, 0, 0, 0]
[0, 0, 3, 3, 3, 3]
[0, 0, 3, 4, 4, 7]
[0, 0, 3, 4, 5, 7]
[0, 0, 3, 4, 5, 7]

(5) ANALYSIS and INFERENCE:
- **Time Complexity:** $O(NW)$
- **Space Complexity:** $O(NW)$
- **Inference:** The DP table stores the best revenue for every application prefix and resource capacity, ensuring that only complete applications are selected to satisfy the 0/1 condition and maximize revenue under limits.
