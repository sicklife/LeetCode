/*
 * FindMedian.cpp
 *
 *  Created on: Mar 11, 2013
 *      Author: root
 */

#include "FindMedian.h"
#include <algorithm>
#include <iostream>
#include <stdio.h>
using namespace std;
FindMedian::FindMedian() {
	// TODO Auto-generated constructor stub
     m=0;
     n=0;
}


int FindMedian::FindMedianTwoSortedArrays(int A[],int m,int B[],int n){
	int location;
	int *a,*b;
	a=A;
	b=B;
	if((m+n)%2==1)location=(m+n)/2+1;
	else location=(m+n)/2;
	int med;
	int pa=0,pb=0,i=0;
	for(i=0;i<location;i++){
	if(a[pa]<b[pb]){
		med=a[pa];
		pa++;
	}
	else{
		med=b[pb];
		pb++;
	}
	}
	return med;
}

FindMedian::~FindMedian() {
	// TODO Auto-generated destructor stub
}

int main(){
	FindMedian test;
	int first[]={1,2,6,6,7};
	int second[]={3,7,9,30,50};
	int result;
	result=test.FindMedianTwoSortedArrays(first,5,second,4);
	cout<<result<<endl;
}
