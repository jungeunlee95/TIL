package kr.co.mlec.day04.homework;

/*
  7. ������ ���� ���鼭 �ڵ带 �ۼ��Ͻÿ�.
 
   �����̰� 100M������ �칰�� �������ϴ�
   �����̴� �ѽð��� 5M�ӵ��� �칰�� �������ϴ�
   �ö� ���̰� 50M�̸��� ���� �ѽð��� 1M�� �̲�������,
   �ö� ���̰� 50M�̻��� ���� �ѽð��� 2M�� �̲������ϴ�
   �����̰� ��ð� ���� �칰�� Ż���ϴ��� �ڵ带 �ۼ�
   
   < ��°�� >
   [1�ð���] �����̰� �ö� �� ���� : 4M
   [2�ð���] �����̰� �ö� �� ���� : 8M
   ...
   [XX�ð���] �����̰� �ö� �� ���� : 100M, 101M, 102M
 */

public class HWMain07 {

	public static void main(String[] args) {

		int height = 0, time = 0;
		int move= 5;
		System.out.println("< ��°�� >");
		while(true) {
			time++;
			height +=move;
			if(height<50) {
				height--;
			}else {
				height-=2;
			}
			
			System.out.println("[ "+time+"�ð� �� ] �����̰� �ö� �� ���� : "+ height +"M");
			if(height>100) break;
		}
		

	}

}






