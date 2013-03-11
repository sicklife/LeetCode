/*
 * TwoSumSol.h
 *
 *  Created on: Mar 11, 2013
 *      Author: root
 */
#include <vector>
#include <iostream>
#include <stdio.h>
#ifndef TWOSUMSOL_H_
#define TWOSUMSOL_H_
using namespace std;

class TwoSumSol {
public:
	TwoSumSol();
	virtual ~TwoSumSol();
    vector<int> twoSum(vector<int> &numbers, int target) ;
private:
    	vector<int> numbers;
    	int target;
};

#endif /* TWOSUMSOL_H_ */
