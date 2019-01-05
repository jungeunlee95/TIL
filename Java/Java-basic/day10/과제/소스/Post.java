package kr.co.mlec.day11.homework;

public class Post {
	private int num;
	private String name;
	private String date;
	private String title;
	
	public Post(int num, String name, String date, String title) {
		super();
		this.num = num;
		this.name = name;
		this.date = date;
		this.title = title;
	}
	
	public void setNum(int num) {
		this.num = num;
	}
	
	public void setName(String name) {
		this.name = name;
	}
	
	public void setDate(String date) {
		this.date = date;
	}

	public void setTitle(String title) {
		this.title = title;
	}

	@Override
	public String toString() {
		return num + "\t" + name + "\t" + date + "\t" + title;
	}
	
	
	
}
