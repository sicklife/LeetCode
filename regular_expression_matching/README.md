## Regular Expression Matching

Implement regular expression matching with support for '.' and '*'.
```bash
'.' Matches any single character.
'*' Matches zero or more of the preceding element.
```
The matching should cover the entire input string (not partial).

The function prototype should be:
```bash
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("aa", "a*") → true
isMatch("aa", ".*") → true
isMatch("ab", ".*") → true
isMatch("aab", "c*a*b") → true
```
Run the program:
  ```bash
python regular_expression_matching.py "aa" "abab"
python regular_expression_matching.py "aa" "a*"
  ```
