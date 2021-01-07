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
- Required fast runtime: had hidden runtime threshold
- Input range: 3<= n <= 200
## Approach and Learning ##
### BruteForce.py ###
- Initial approach to get solution without regard for runtime. Recursively iterate through all possibilities of stair level and count which possibilities end with n stair cases.
- Realized that problem can be slightly simplified here by only checking n/2 (or n/2-1 if even) blocks for the first level, since the next level had to be >
- Got correct answers, but when analyzing runtime computer reached ~ 8 seconds to find possibilities for n=100 blocks. See BruteForce_Runtime.png for runtime gaph 
