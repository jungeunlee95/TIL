package kr.co.mlec.day06.homework;

/*
 - �Ʒ��� ������ �����ϴ� StringUtil Ŭ������ �ۼ��մϴ�.
  MethodMain Ŭ������ �������� �ʰ� StringUtil Ŭ�������� �ۼ��մϴ�.
1. �ϳ��� ���ڸ� �Է¹޾� �ش� ���ڰ� �빮���̸� true �� ��ȯ�ϴ� isUpperChar( char c ) �޼ҵ带 �ۼ��Ͻÿ� 
2. �ϳ��� ���ڸ� �Է¹޾� �ش� ���ڰ� �ҹ����̸� true�� ��ȯ�ϴ� isLowerChar(char c) �� �ҵ带 �ۼ��Ͻÿ� 
3. �ΰ��� ���ڸ� �Է¹޾� ū���� ��ȯ�ϴ� max( int i, int j) �޼ҵ带 �ۼ��Ͻÿ� 
4. �ΰ��� ���ڸ� �Է¹޾� �������� ��ȯ�ϴ� min(int i, int j) �޼ҵ带 �ۼ��Ͻÿ�  
5. ���ڿ��� �Է¹޾� �Ųٷ� �����ϴ� reverseString( String str ) �޼ҵ带 �ۼ��Ͻÿ� 
6. ���ڿ��� �Է¹޾� �빮�ڷ� �����ϴ� toUpperString( String str ) �޼ҵ带 �ۼ��Ͻÿ� 
7. ���ڿ��� �Է¹޾� �ҹ��ڷ� �����ϴ� toLowerString( String str ) �޼ҵ带 �ۼ��Ͻÿ�
 */
public class StringUtil {

	// �ϳ��� ���ڸ� �Է¹޾� �ش� ���ڰ� �빮���̸� true �� ��ȯ�ϴ� isUpperChar( char c ) �޼ҵ带 �ۼ��Ͻÿ�
	boolean isUpperChar(char c) {
		if (c >= 'A' && c <= 'Z')
			return true;
		else
			return false;
	}

	// �ϳ��� ���ڸ� �Է¹޾� �ش� ���ڰ� �ҹ����̸� true�� ��ȯ�ϴ� isLowerChar(char c) �� �ҵ带 �ۼ��Ͻÿ�
	boolean isLowerChar(char c) {
		if (c >= 'a' && c <= 'z')
			return true;
		else
			return false;
	}

	// �ΰ��� ���ڸ� �Է¹޾� ū���� ��ȯ�ϴ� max( int i, int j) �޼ҵ带 �ۼ��Ͻÿ�
	int max(int i, int j) {
		return i > j ? i : j;
	}
	
	//�ΰ��� ���ڸ� �Է¹޾� �������� ��ȯ�ϴ� min(int i, int j) �޼ҵ带 �ۼ��Ͻÿ�
	int min(int i, int j) {
		return i < j ? i : j;
	}
	
	//���ڿ��� �Է¹޾� �Ųٷ� �����ϴ� reverseString( String str ) �޼ҵ带 �ۼ��Ͻÿ� 
	String reversString(String str) {
		char[] ch = new char[str.length()];
		for(int i = str.length()-1; i>=0; i--) {
			ch[i] = str.charAt(str.length()-i-1);
		}
		return new String(ch);
	}
	
	//���ڿ��� �Է¹޾� �빮�ڷ� �����ϴ� toUpperString( String str ) �޼ҵ带 �ۼ��Ͻÿ�
	String toUpperString(String str) {
		char[] ch = new char[str.length()];
		for(int i=0; i<str.length(); i++) {
			if(str.charAt(i)>='a' && str.charAt(i)<='z') {
				ch[i] = (char)(str.charAt(i) - 32);
			}else {
				ch[i] = str.charAt(i);
			}
		}
		return new String(ch);
	}
	
	//���ڿ��� �Է¹޾� �ҹ��ڷ� �����ϴ� toLowerString( String str ) �޼ҵ带 �ۼ��Ͻÿ�
	String toLowerString(String str) {
		char[] ch = new char[str.length()];
		for(int i=0; i<str.length(); i++) {
			if(str.charAt(i)>='A' && str.charAt(i)<='Z') {
				ch[i] = (char)(str.charAt(i) + 32);
			}else {
				ch[i] = str.charAt(i);
			}
		}
		
		return new String(ch);
	}
}














