package kr.co.mlec.day04.homework;

/*
6-1. 2 - 9사이의 구구단 출력(한라인에 3단씩 출력)
 
    *** i단 ***   *** i+k단 ***   *** i+k단 ***
    i * j = 2      i * j = 3     i * j = 4
    ...
    
    *** 5단 ***   *** 6단 ***   *** 7단 ***
    ...
    
    *** 8단 ***   *** 9단 ***
    ...
    8 * 1 = 72   9 * 1 = 81
    
    for(int i = 2; i <= 9; ) {}
    반복문을 최대 3개만 사용 
*/

public class HWMain06_2 {

	public static void main(String[] args) {

		for (int i = 2; i < 9; i += 3) {
			for (int j = 0; j < 10; j++) { // 단 당 10줄
				for(int k = 0; k<3; k++) {
					if(j==0) {
						if(i+k==10) break;
						System.out.print("*** "+(i+k)+"단 ***  ");
					}else {
						if(i+k==10) break;
						System.out.print(" " + (i+k) + " * " + j + " = " + (i+k) * j +" ");
					}
				}
				System.out.println();
			}
			System.out.println();
		}
	}
}
