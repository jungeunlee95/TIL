package kr.co.mlec.day08.homework;

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

	@Override
	public int area() {
		return height*width/2;
	}

	@Override
	public double cArea() {
		return 0;
	}



}
