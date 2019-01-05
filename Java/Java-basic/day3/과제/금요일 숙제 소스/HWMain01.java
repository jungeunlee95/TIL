package kr.co.mlec.day04.homework;
/*
    1 ~ 100사이의 홀수 출력
	1 3 5 7 , ... , 97, 99
 */
public class HWMain01 {

	public static void main(String[] args) {

		/*for (int i = 0; i < 100; i++) {
			if (i % 2 == 1) System.out.print(i + "  ");
		}*/
		
		for(int i=1; i<100; i+=2) {
			System.out.print(i + " ");
		}
	}

}
