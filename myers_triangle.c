#include <stdio.h>
#include <stdlib.h>

//Scalene triangle 不等辺三角形
//Isosceles triangle 二等辺三角形
//Equilateral triangle 正三角形

enum Triangle{Scalene, Isosceles, Equilateral};
int determine_triangle_types(int num1, int num2, int num3);

int main(int argc, char *argv[]){

  switch(determine_triangle_types(atoi(argv[1]), atoi(argv[2]), atoi(argv[3]))){
    case 0:
      printf("Scalene\n");
      break;
    case 1:
      printf("Isosceles\n");
      break;
    case 2:
      printf("Equilateral\n");
      break;
    case -1:
      printf("Illegal triangle\n");    
  }
  
  return 0;

}

int determine_triangle_types(int num1, int num2, int num3){

  if((num1 + num2 > num3 && num1 + num3 > num2 && num2 + num3 > num1)
      && (num1 > 0 && num2 > 0 && num3 > 0)) {
    if(num1 == num2 && num2 == num3) {
      return Equilateral;
    }else if(num1 == num2 || num2 == num3 || num1 == num2) {
      return Isosceles;
    }else{
      return Scalene;
    }
  }else{
    return -1;
  }

}
