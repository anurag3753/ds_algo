## Maximum Subarray Sum (Kadane's Algorithm)
    - TC = O(n)
    - SC = O(1)
    - Logic : For every element, find out max subarray that must end with this element AND overall result is max of these values.
        - Two vars is sufficient to keep track (maxEnding, res)
        - maxEnding[i] = max(maxEnding[i-1] + arr[i], arr[i]) 
