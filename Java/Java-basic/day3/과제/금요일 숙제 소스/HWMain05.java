package kr.co.mlec.day04.homework;

/*
5. ������ ���
   *** 2�� ***
   2 * 1 = 2
   2 * 2 = 4
   ...
   2 * 9 = 18
   
   *** 3�� ***
   ...
   
   9 * 9 = 81

*/

public class HWMain05 {

	public static void main(String[] args) {
		
		for(int i=1; i<10; i++) {
			System.out.println("*** " + i + "�� ***");
			for(int j=1; j<10; j++) {
				System.out.println(i + " * " + j + " = " + i * j);
			}
			System.out.println();
		}

	}

}
