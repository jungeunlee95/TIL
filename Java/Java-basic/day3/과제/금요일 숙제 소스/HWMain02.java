package kr.co.mlec.day04.homework;

/*
 2. 100 ~ 1 사이의 짝수 출력
	100 98  96, ... , 4, 2
 */

public class HWMain02 {

	public static void main(String[] args) {

		/*for(int i=100; i>0; i--) {
			if(i%2==0) System.out.print(i+" ");
		}*/
		
		for(int i=100; i>0; i-=2) {
			System.out.print(i+" ");
		}

	}

}
