package Day2Homework;

import java.util.Scanner;

/*
 *4. ȭ�鿡�� �ϳ��� ������ �Է� �ް� ������ ���� ���� �Է� ���� ���� ��� �������� ȭ�鿡 ����Ͻÿ�
������ �Է��ϼ���  :  10
���� ���� �Է��ϼ���  :  7
�� : 1
������ : 


 */
public class Number4 {
        public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		System.out.print("������ �Է��ϼ��� : ");
		int num = sc.nextInt();
		
		System.out.print("���� ���� �Է��ϼ��� : ");
		int num2 = sc.nextInt();
		
		//System.out.println("�� : " + (num/num2) + ", ������ : " + (num%num2));
		 if(num2 == 0) {
		    	System.out.println("0���� ���� �� �����ϴ�.");
		    }  else if(num == 0) { 
		    	System.out.println("0�� ���� �� �����ϴ�.");
		    }  else {
		    	System.out.println("�� : " + (num/num2) + ", ������ : " + (num%num2));
	        } 
		 
       }
}
