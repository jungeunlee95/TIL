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
			System.out.println("번호\t작성자\t수정일\t\t제목");
			for(int i=0; i<list.size(); i++) {
				System.out.println(list.get(i));
			}
		}else {
			System.out.println("등록된 게시글이 없습니다.");
		}
	}
	public void showPost() {		
		if(!list.isEmpty()) {
			num = scanInt("조회할 글 번호");
			System.out.println("번호\t작성자\t수정일\t\t제목");
			System.out.println(list.get(num-1));
		}else {
			System.out.println("등록된 게시글이 없습니다.");
		}
	}
	
	public void add() {
		num = list.size() +1;
		name = scanLine("작성자");
		title = scanLine("제목");
		date = modifiedDate();
		
		list.add(new Post(num, name, date, title));
		System.out.println("등록 완료");
	}
	
	public void rewrite() {
		num = scanInt("수정할 글 번호");
		name = scanLine("작성자");
		title = scanLine("제목");
		date = modifiedDate();
	
		Post p = list.get(num-1);
		p.setTitle(title);
		p.setName(name);
		p.setDate(date);
	}
	
	public void delete() {
		num = scanInt("삭제할 글 번호");
		list.remove(num-1);
		System.out.println("삭제 완료");
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
		System.out.println("*** 메뉴 ***");
		System.out.println("1. 전체 게시글 조회");
		System.out.println("2. 글번호 조회");
		System.out.println("3. 글등록");
		System.out.println("4. 글수정");
		System.out.println("5. 글삭제");
		System.out.println("0. 종료");
	}
}
