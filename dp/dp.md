## Dynamic Programming

- Base Condition:
    - Think of smallest valid input.
```cpp
// 0/1 Knapsack
// i/p: int wt[], int val[], int n, int W

int knapsack(int wt[], int val[], int n, int W) {
    if (n == 0 || wt == 0){
        return 0;    
    }
}

// Think of smallest possible input for wt/val :- ye array hai, har baar subproblem mai hum iska size reduce kar denge
// to lowest valid size kya ho sakta hai :- n == 0
// Tum koi store gaye, aur pata chala waha koi item hi nahi hai, to kya le ja paaoge. so max profit = 0 

// Ek aur hai Wt, ye kya hai bag ka wt, to isme lowest kya ho sakta hai :- 0 
// Tum store gaye aur pata chala waha to sara saaman bhari hai, aur tumhara bag us wt ko hold nahi kar sakta, to bhi kuch nahi le ja paaoge. Hence, max profit = 0
```