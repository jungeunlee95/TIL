package kr.co.mlec.day07.homework;

/**
 * �ﰢ���� ���̸� ����ϱ� ���� Area�� ��ӹ޴� Ŭ���� => Area�� �ٸ� �� : ���̸� ������ ����
 * 
 * @author BIT
 *
 */
public class TriArea extends Area {

	public TriArea(int height, int width) {
		super(height, width);
	}

	public int area() {
		int area = super.area() / 2;
		return area;
	}

}
