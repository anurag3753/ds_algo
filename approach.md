# Approach to solve coding test/challenges in Interview
- Read the instructions
    - Get mentally prepared (MCQs, Coding Questions etc)
- Time Allotted
- Number of Questions
- If each problem has equal weightage ??
- If each has same difficulty level (if provided)

# As per experience
- If three questions are there and time is 90 min then:
    - q1 (easy)            50 score
    - q2 (medium)          100 score
    - q3 (hard)            150 score

Then x + 2x + 3x = 90 , i.e x = 15
- It means we need to give 15 min to q1, 30 min to q2 and 45 min to q3
- +5 min, -5min is delta

- If they are of equal score:
    - Then we would have given equal time to all three questions

- Time Management is most critical

# Question Description
- Problem Statement
    - Make habitual of understand from PS, that how i/p is getting converted to o/p
    - Read it carefully (most important, read it carefully till you understand)
        - 2 types    
            - story questions (you need to convert it to straightforward questions. Ex codechef questions)
            - straightforward questions
- Input
    - Like Hackerrank (just write your function)
    - Like Hackerearth (do everything from ground up)
    - Even testcase passing also has points. Corner cases have more points than easy cases
- Output
    - All testcases should pass
    - Think of corner cases, edge cases
    - think how code will perform on big numbers
- Explaination of how to get o/p from i/p (OPTIONAL)
- Constraints
    - It tells us, what type of data type to choose for our values (like int, long long)
    - Some provide time limit per testcase, some provide time limit for entire question
    - Machine power is ~ 10<sup>8</sup> per second
    - Suppose Time limit per testcase is given as 2 sec , It means we should not exceed more than 2 * 10<sup>8</sup>  operations in our code
    - `#` of operations <= `#` seconds * 10<sup>8</sup>
    - From constraints, identify the time-complexity of code. And then think in that directions like what DS/Algorithm can be used. Check the below Table
    - You should do these calculations first, and not even needed to read the problem statements to indentify the time complexity code that we need to write

    - For O(2<sup>N</sup>) code, we should understand that they are asking for exponential approach. And recursion is exponential approach.
    - For O(N), it is linear. You might be using stacks/hash map etc to get it into linear
    - For O(10<sup>18</sup>) Binary Search needs to be used.

| Constraints (N Max) | TC               |
|---------------------|------------------|
| 10<sup>18</sup>     | O(logN)          |
| 10<sup>8</sup>      | O(N)             |
| 10<sup>6</sup>      | O(NlogN)         |
| 10<sup>4</sup>      | O(N<sup>2</sup>) |
| 500                 | O(N<sup>3</sup>) |
| 85-90               | O(N<sup>4</sup>) |
| 20                  | O(2<sup>N</sup>) |
| 11                  | O(N!)            |

# How to Debug ??
- Never read the code while debugging
- Try to identify the parts in the code. i.e. divide your code into multiple functions.
- First dry run the logic in pen and paper using some input
- After dry run you thought logic is correct and you finally write the code
- Then during the run. You did not get the expected o/p. So,
- Use test custom input for debugging and provide it the testcase that you used for dry run


## Final Tips: Main Goal is to narrow down the search space in code (4 points)
- Provide custom i/p + Re-run the logic on pen-paper to identify if logic is correct or not.
- Provide print statements at major logic divide points
- If code is divided into multiple functions, then try to stub/mock functions one by one to identify the faulty function.
- comment some part of code:
    - suppose if you get `segfault` from your code, and you want to identify what is causing it. Then comment some part of code and then check the output, to see if you are able to run the code now. Try this way for multiple code segments.