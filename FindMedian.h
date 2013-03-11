/*
 * FindMedian.h
 *
 *  Created on: Mar 11, 2013
 *      Author: root
 */
#include <iostream>
#include <stdio.h>
#ifndef FINDMEDIAN_H_
#define FINDMEDIAN_H_

class FindMedian {
public:
	FindMedian();
	virtual ~FindMedian();
	int FindMedianTwoSortedArrays(int A[],int m,int B[],int n);
private:
	int A[];
	int m;
	int B[];
	int n;
};

#endif /* FINDMEDIAN_H_ */
