package kr.co.mlec.day07.homework;

/**
 * �غ��� ���̰� �ٸ� ���簢���� ���̸� ���ϱ� ���� Ŭ����
 * 
 * @author BIT
 *
 */
public class Area {

	private int height;
	private int width;

	public Area(int height) {
		this.height = height;
		this.width = height;
	}

	public Area(int height, int width) {
		this.height = height;
		this.width = width;
	}

	public int area() {
		return height * width;
	}

}
