package kr.co.mlec.day04.homework;

import java.util.Scanner;

/*
3. ������ ����� ���̴� ���α׷� �ۼ�
 2 - 9������ ���� �Է� : 5
 
 // 1�ܰ�
 <5�� ����� ������ ���� ��� >
 1  2  3  4  6  7  8  9  11  12 , ..., 97  98  99
 
  // 2�ܰ�
 <5�� ����� ������ ���� ��� >
 1  2  3  4  6  
 7  8  9  11  12 
 , ..., 97  98  99	
 
*/
public class HWMain03_2 {

	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		
		System.out.print("2 - 9 ������ ���� �Է� : ");
		int num = scan.nextInt();
		int cnt = 0;
		
		for(int i=1; i<=100; i++) {
			if(i%num != 0) {
				System.out.print(i+"  ");
				cnt++;
				if(cnt == 5) {
					System.out.println();
					cnt = 0;
				}
			}
		}

		scan.close();
		
	}

}
