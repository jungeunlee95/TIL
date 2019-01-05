package kr.co.mlec.day06.homework;

/*
 - 아래의 내용을 만족하는 StringUtil 클래스를 작성합니다.
  MethodMain 클래스는 변경하지 않고 StringUtil 클래스만을 작성합니다.
1. 하나의 문자를 입력받아 해당 문자가 대문자이면 true 를 반환하는 isUpperChar( char c ) 메소드를 작성하시오 
2. 하나의 문자를 입력받아 해당 문자가 소문자이면 true를 반환하는 isLowerChar(char c) 메 소드를 작성하시오 
3. 두개의 숫자를 입력받아 큰수를 반환하는 max( int i, int j) 메소드를 작성하시오 
4. 두개의 숫자를 입력받아 작은수를 반환하는 min(int i, int j) 메소드를 작성하시오  
5. 문자열을 입력받아 거꾸로 변경하는 reverseString( String str ) 메소드를 작성하시오 
6. 문자열을 입력받아 대문자로 변경하는 toUpperString( String str ) 메소드를 작성하시오 
7. 문자열을 입력받아 소문자로 변경하는 toLowerString( String str ) 메소드를 작성하시오
 */
public class StringUtil {

	// 하나의 문자를 입력받아 해당 문자가 대문자이면 true 를 반환하는 isUpperChar( char c ) 메소드를 작성하시오
	boolean isUpperChar(char c) {
		if (c >= 'A' && c <= 'Z')
			return true;
		else
			return false;
	}

	// 하나의 문자를 입력받아 해당 문자가 소문자이면 true를 반환하는 isLowerChar(char c) 메 소드를 작성하시오
	boolean isLowerChar(char c) {
		if (c >= 'a' && c <= 'z')
			return true;
		else
			return false;
	}

	// 두개의 숫자를 입력받아 큰수를 반환하는 max( int i, int j) 메소드를 작성하시오
	int max(int i, int j) {
		return i > j ? i : j;
	}
	
	//두개의 숫자를 입력받아 작은수를 반환하는 min(int i, int j) 메소드를 작성하시오
	int min(int i, int j) {
		return i < j ? i : j;
	}
	
	//문자열을 입력받아 거꾸로 변경하는 reverseString( String str ) 메소드를 작성하시오 
	String reversString(String str) {
		char[] ch = new char[str.length()];
		for(int i = str.length()-1; i>=0; i--) {
			ch[i] = str.charAt(str.length()-i-1);
		}
		return new String(ch);
	}
	
	//문자열을 입력받아 대문자로 변경하는 toUpperString( String str ) 메소드를 작성하시오
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
	
	//문자열을 입력받아 소문자로 변경하는 toLowerString( String str ) 메소드를 작성하시오
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














