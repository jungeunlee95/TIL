package Day2Homework;
//QQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ
import java.util.Scanner;

/*
 *2. 3661�ʰ� �� �ð� �� �� �� ������ ȯ���ؼ� ����Ͻÿ� 
������ : 1�ð� 1�� 1��
�ʸ� �Է��Ͻÿ�. 0000��
=00�ð� 00�� 00��

{{{{{{{{�ؾ��� ��}}}}}}}}
1. ����� �Է� �ޱ� : Scanner�Լ� ��� "�ʸ� �Է��Ͻÿ�" 
2.�� = "�Էµ� ��"�� 60���� ���� ������
    �� = ("�Էµ� ��"�� 60���� ���� ������)�� 60���� ���� ������ 
  �ð� = ("�Էµ� ��"�� 60���� ���� ��)�� 60���� ���� ��
3."�Էµ� ���� �ð���~ �Դϴ�"    
 */
public class Number2 {
	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		
		System.out.print("�ʸ� �Է��ϼ���.");
		
		int num =  sc.nextInt();
		int second = num % 60;
		int minute = second % 60;
		int hour = (num / 60 ) / 60;
		
		System.out.println("�� ���� �ð��� : " + hour + "�ð�" + minute + "��" + second + "��" + "�Դϴ�.");
		
/*�߰� ����
ex) 2889��  -0�ð� 48�� 32��  -> �̷����� �ð� �����ϰ� �� �ʸ� �߰�
ex) 12�ʸ� -> �ʸ��߰�
 
 ���� ���� 0 �̸� ǥ��������. 
 
*/
//		if(second == 0) {
//			System.out.println("�� ���� �ð��� : " + hour + "�ð�" + minute + "��" + "�Դϴ�.");
//	    }  else if(minute == 0) { 
//	    	System.out.println("�� ���� �ð��� : " + hour + "�ð�" + second + "��" + "�Դϴ�.");
//	    }  else if(hour == 0 ){
//	    	System.out.println("�� ���� �ð��� : " + minute + "��" + second + "��" + "�Դϴ�.");
//        }  else {
//        	System.out.println("�� ���� �ð��� : " + hour + "�ð�" + minute + "��" + second + "��" + "�Դϴ�.");
//        }
		
	}

}
		
