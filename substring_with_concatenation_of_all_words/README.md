##Substring with Concatenation of All Words

You are given a string, S, and a list of words, L, that are all of the same length. Find all starting indices of substring(s) in S that is a concatenation of each word in L exactly once and without any intervening characters.
```
For example, given:
S: "barfoothefoobarman"
L: ["foo", "bar"]
```

You should return the indices: [0,9].
(order does not matter).


The brute force method works here. Assume the hash function is O(n). Let the length of S be M, the length of L be N, and the length of each word in L be P, as intruduced in other solutions, the worst time complexity O(M*N*P) is accepted by the OJ system. It could be optimized by using [Caterpillar](https://codility.com/media/train/13-CaterpillarMethod.pdf) method. The given optimization solution need O(M*P).

Run the program:
```
python sutstring_with_concatenation_of_allwords.py
```

