package Day2Homework;
//QQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ

import java.util.Scanner;

/*
 *ȭ�鿡�� ���ĺ��� �Է� �޾� �빮�ڴ� �ҹ��ڷ� �ҹ��ڴ� �빮�ڷ� ����ϴ� ���α׷��� �ۼ��Ͻÿ�
�Է�(���ĺ�) : a
����� �� : A
����> ȭ�鿡�� ���� ���ڿ����� �� ���� ��������
String inputStr = sc.nextLine( );
char c = inputStr.charAt(0);

-�ҹ��ڿ� �빮���� �ƽ�Ű �ڵ��� ���̴� 32
65 <= char <= 90 or 'A' <= char <= 'Z'  =>�빮��
97 <= char <= 122 or 'a' <= char <= 'z'  =>�ҹ���

  A -> a�� ������� 32�� ���ϰ�
  a -> A�� ������� 32�� ����

 */

public class Number7 {
	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		String inputStr = sc.nextLine( );
		char c = inputStr.charAt(0);
		
		if('A' <= c && c<= 'Z') {
			System.out.println((char)(c-'A'+'a'));
		}
		
		
		
		
	}
}
