package kr.co.mlec.day11.homework;

import java.util.List;
import java.util.Scanner;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Date;

public class Board {
	List<Post> list = new ArrayList<>();
	Scanner scan = new Scanner(System.in);
	int num;
	String name;
	String date;
	String title;
	
	public void showAll() {
		
		if(!list.isEmpty()) {
			System.out.println("��ȣ\t�ۼ���\t������\t\t����");
			for(int i=0; i<list.size(); i++) {
				System.out.println(list.get(i));
			}
		}else {
			System.out.println("��ϵ� �Խñ��� �����ϴ�.");
		}
	}
	public void showPost() {		
		if(!list.isEmpty()) {
			num = scanInt("��ȸ�� �� ��ȣ");
			System.out.println("��ȣ\t�ۼ���\t������\t\t����");
			System.out.println(list.get(num-1));
		}else {
			System.out.println("��ϵ� �Խñ��� �����ϴ�.");
		}
	}
	
	public void add() {
		num = list.size() +1;
		name = scanLine("�ۼ���");
		title = scanLine("����");
		date = modifiedDate();
		
		list.add(new Post(num, name, date, title));
		System.out.println("��� �Ϸ�");
	}
	
	public void rewrite() {
		num = scanInt("������ �� ��ȣ");
		name = scanLine("�ۼ���");
		title = scanLine("����");
		date = modifiedDate();
	
		Post p = list.get(num-1);
		p.setTitle(title);
		p.setName(name);
		p.setDate(date);
	}
	
	public void delete() {
		num = scanInt("������ �� ��ȣ");
		list.remove(num-1);
		System.out.println("���� �Ϸ�");
		for(int i =0; i<list.size();i++) {
			Post p = list.get(i);
			p.setNum(i+1);
		}
	}
	
	public int scanInt(String msg) {
		System.out.print(msg + " : ");
		int num = scan.nextInt();
		scan.nextLine();
		return num;
	}
	
	public String scanLine(String msg) {
		System.out.print(msg + " : ");
		return scan.nextLine();
	}
	
	public String modifiedDate() {
		SimpleDateFormat sdf = new SimpleDateFormat("yyyy-MM-dd");
		return sdf.format(new Date());
	}
	
	public void print() {
		System.out.println("*** �޴� ***");
		System.out.println("1. ��ü �Խñ� ��ȸ");
		System.out.println("2. �۹�ȣ ��ȸ");
		System.out.println("3. �۵��");
		System.out.println("4. �ۼ���");
		System.out.println("5. �ۻ���");
		System.out.println("0. ����");
	}
}
