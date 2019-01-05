package kr.co.mlec.day08.homework;

/**
 * �غ��� ���̰� �ٸ� ���簢���� ���̸� ���ϱ� ���� Ŭ����
 * 
 * @author BIT
 *
 */
public abstract class Area {

	public int height;
	public int width;

	public Area(int height) {
		this.height = height;
		this.width = height;
	}

	public Area(int height, int width) {
		this.height = height;
		this.width = width;
	}

	public abstract int area();
	public abstract double cArea();

}
