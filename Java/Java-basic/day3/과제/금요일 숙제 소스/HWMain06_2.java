package kr.co.mlec.day04.homework;

/*
6-1. 2 - 9������ ������ ���(�Ѷ��ο� 3�ܾ� ���)
 
    *** i�� ***   *** i+k�� ***   *** i+k�� ***
    i * j = 2      i * j = 3     i * j = 4
    ...
    
    *** 5�� ***   *** 6�� ***   *** 7�� ***
    ...
    
    *** 8�� ***   *** 9�� ***
    ...
    8 * 1 = 72   9 * 1 = 81
    
    for(int i = 2; i <= 9; ) {}
    �ݺ����� �ִ� 3���� ��� 
*/

public class HWMain06_2 {

	public static void main(String[] args) {

		for (int i = 2; i < 9; i += 3) {
			for (int j = 0; j < 10; j++) { // �� �� 10��
				for(int k = 0; k<3; k++) {
					if(j==0) {
						if(i+k==10) break;
						System.out.print("*** "+(i+k)+"�� ***  ");
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
