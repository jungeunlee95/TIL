package Day3Homework;

/*
             -  *  -
********* 1  0  9  0  10-i
-*******  2  1  7  1  9-i
--*****   3  2  5  2  8-i
---***    4  3  3  3  7-i
----*     5  4  1  4  6-i         

*�� ������ 0,1,2,3,4 ������ ������� 
             
 */
public class Number1 {

	public static void main(String[] args) {
		
		for(int i = 1; i <= 5; i++) {    
			for(int j = 1; j <= 10-i; j++) {  //*����
				if(i > j) {                 //5����� '-' ������ �ϳ��� �þ
					System.out.print('-');
				} else {                    //6����ʹ� *������ �ϳ��� �پ����
					System.out.print('*');
				}
				
			}
			System.out.println();
		}
	}
}