/*
 * TwoSumSol.cpp
 *
 *  Created on: Mar 11, 2013
 *      Author: yning
 */

#include <stdio.h>
using namespace std;
vector<int> twoSum(vector<int> &numbers, int target) {
        int len = numbers.size();
        vector<int> index;
        vector<int> substract (len);
        for (int i = 0; i < len; i++){
        	int result = target - numbers[i];
        	if (result >= 0) {
        		for (int j = i + 1; j < len; j++) {
        			if (numbers[j] == result){
        				index.push_back(i);
        				index.push_back(j);
        			}
        		}
        	}
        }
   return index;
}
int main(){
	vector<int> resultindex;
	int myints[4] = {2,7,8,9};
	vector<int> inputarray(myints, myints + sizeof(myints) / sizeof(int));
	resultindex = twoSum(inputarray,17);
	for (int i = 0; i < resultindex.size(); i++)
		printf("index:%d, ", resultindex[i]);
}

