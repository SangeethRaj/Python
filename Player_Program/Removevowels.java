package removeVowels;
import java.util.*;
public class RemoveVowels {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
	Scanner s=new Scanner (System.in);
	String a=s.next();
	int l=a.length();
	for(int i=l-1;i>=0;i--) {
		switch(a.charAt(i)) {
		case 'a':
			break;
		case 'e':
			break;
		case 'i':
			break;
		case 'o':
			break;
		case 'u':
			break;
			default: System.out.print(a.charAt(i));
		}
	}
	}
}
