
package Day3Homework;
/*
 
----*         5-1
---***        6-3
--*****       7-5
-*******      8-7
*********     9-9

-*******      8-7
--*****       7-5   
---***        6-3
----*         5-1
 */

public class Number02 {

	public static void main(String[] args) {
		for(int i = 1; i <= 9; i++) {
			for(int j = 1;j<=9; j++ ) {
				if (i<=5) {                     //���� ����
					if (i+j<=5) {
						System.out.print('-');  //���� ���� ����
					}else if (j-i >= 5) {
						System.out.print("-");  //���� �� �� ����
					} else {
						System.out.print("*");  //���� �������� ���� �������� ��� *
					}
					
				}else if (i>5) {                //�Ʒ���, i�� 6 �̻󿵿�
					if(i-j>=5) {
						System.out.print('-');  //�Ʒ��� ���� ����
					}else if (i+j >= 15) {
						System.out.print('-');  //�Ʒ��� ������ ����
					}else {
						System.out.print('*');  //�Ʒ��� ���� �������� *��
					}
				}
		} System.out.println();

	}
	}
}

