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
## Approach and Learning ##
### BruteForce.py ###
- Initial approach to get solution without regard for runtime. Recursively iterate through all possibilities of blocks per stair level (given the next level blocks > current level blocks) and count which possibilities end with n blocks.
- Realized that problem can be slightly simplified here by only checking n/2 (or n/2-1 if even) blocks for the first level, since anything more than halfway-1 would break the rule of every subsequent level > than previous
- Got correct answers, but when analyzing runtime computer reached ~ 8 seconds to find possibilities for n=100 blocks. See BruteForce_Runtime.png for runtime gaph 
### Subtree Aggregation ###
- I went back to the drawing board and worked on small sample cases to find patterns in the way staircase number increased.
- Started to see a tree structure for all possible staircases, needed a way to quickly calculate number of nodes in the tree. This meant I needed to look at the problem more mathematically
- 
- Runtime: look at SubtreeAgg_Runtime.png, much better performance. Takes less than 1 second to calculate possibilites for n=100 blocks. But still not good enough to quickly calculate 200
### Subtree Aggregation ###
