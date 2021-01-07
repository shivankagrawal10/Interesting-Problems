# Level 3: Problem 1 #

## Problem: Given n blocks how many possible stair cases can be generated ##
Where stair case is defined as:
- Using all n blocks
- Every Staircase has at least 2 steps
- Every level must be greater than the previous (ex. if current level of stairs is 3 then next must be >= 4)

Example:
Given 3 blocks, 1 staircase is possible
<pre>
%
% %
</pre>
Given 5 blocks, 2 staircase are possible
<pre>
%       
%       %
%       % %
% %     % %
</pre>
## Constraints ##
- Language: Python 2.7.16
- Input range: 3<= n <= 200
- Required fast runtime: had hidden runtime threshold
## Approach ##
### BruteForce.py ###
- Initial approach to get solution without regard for runtime. Recursively iterate through all possibilities of blocks per stair level (given the next level blocks > current level blocks) and count which possibilities end with n blocks.
- Realized that problem can be slightly simplified here by only checking n/2 (or n/2-1 if even) blocks for the first level, since anything more than halfway-1 would break the rule of every subsequent level > than previous
- Performance: Got correct answers, but when analyzing runtime computer reached ~ 10 seconds to find possibilities for n=100 blocks.</br>
See [Brute Force Runtime Graph](1_BruteForce_Runtime.png) for performance gaph 
### Subtree Aggregation ###
- I went back to the drawing board and worked on small sample cases to find patterns in the way staircase number increased.
- Started to see a tree structure for all possible staircases, needed a way to quickly calculate number of nodes in the tree. This meant I needed to look at the problem more mathematically
- <b> Perspective Shift: </b> 
Stopped looking at the problem like blocks and stairs. Started visualizing the problem as finding number of pairs adding up to m (remaining number of blocks) such that the values in the pairs are greater than the number of stairs in the previous level
<pre>
Formula: 
Number of stair case possibilities when m blocks remain and previous stair level was x:
* if m is odd: floor(m/2) - x 
* if m is even: m/2 - 1 - x

Example:
  Scenario:
  n=10
  subcase: x=1 block, m=9 blocks 
  (How many possibilities can be generated when 1 block is used and 9 blocks remain)
  
  Apply:
  floor(m/2) - x = floor(9/2) - 1 = 4 - 1 = 3
  
  Verify:
    9 -> (2,7), (3,6), (4,5) {anything beyond would break the stair construction rule}
  
  Next Step:
  Would repeat process on each produced pair to find total child nodes under it
</pre>
- Runtime: Takes less than 1 second to calculate possibilites for n=100 blocks. But still not good enough to quickly calculate 200, n=130 starts to take 4 seconds and is growing exponentially</br>
See [Subtree Aggregation Runtime Graph](2_SubtreeAgg_Runtime.png) for perfomance graph
### Subtree Aggregation Optimization ###
- Insight: Realized a lot of subtree calculations repeat over large range of n blocks
- Optimization: Applied Memoization to save performance time from repeated calculations 
- Result: Amazing Runtime Performance, Scale is uncomparable to runtime before memoization. n=200 takes between 0.0015 to 0.002 seconds </br>
See [Subtree Aggregation Optimized Runtime Graph](3_SubtreeAggOptimized_Runtime.png) for performance graph
## Learning ##
From this problem, I value 3 lessons I previuosly knew but now have deeper appreciation for. Brainstorming, Breaking the problem down into simpler/familiar mathematical abstractions, Thinking about ways to save rutime performance.
- Process of brainstorming/writing pseudo code before coding gives me a clear roadmap of what I need to implement. Helps clearly separate problem solving from implementation and allows for looking at the problem in unique ways
- Breaking the problem to its bare bone and viewing it from familiar math/data structure constructs elucidates very beautiful solutions and provides a framework for approaching the problem
- Final step of thinking about saving on runtime algorithmically allows for massive advantage when scaling up and dealing with large complex calculations. It makes your solution more applicable for powerful computations.
