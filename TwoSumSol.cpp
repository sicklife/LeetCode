/*
 * TwoSumSol.cpp
 *
 *  Created on: Mar 11, 2013
 *      Author: root
 */

#include "TwoSumSol.h"
#include <stdio.h>
using namespace std;
TwoSumSol::TwoSumSol() {
	// TODO Auto-generated constructor stub
	target=0;
}
vector<int> TwoSumSol::twoSum(vector<int> &numbers, int target) {
        // Start typing your C/C++ solution below
        // DO NOT write int main() function

        int len=numbers.size();
        vector<int> index;
        vector<int> substract (len);
        for(int i=0;i<len;i++){
        	int result=target-numbers[i];
        	if(result>=0){
        		for(int j=i+1;j<len;j++){
        			if(numbers[j]==result){
        				index.push_back(i);
        				index.push_back(j);
        			}
        		}
        	}
        }
   return index;
}
TwoSumSol::~TwoSumSol() {
	// TODO Auto-generated destructor stub
}
int main(){
	TwoSumSol test;
	vector<int> resultindex;
	int myints[4]={2,7,8,9};
	vector<int> inputarray(myints,myints+sizeof(myints)/sizeof(int));
	resultindex=test.twoSum(inputarray,17);
	for(int i=0; i<resultindex.size(); i++)
		printf("index:%d, ",resultindex[i]);
}

