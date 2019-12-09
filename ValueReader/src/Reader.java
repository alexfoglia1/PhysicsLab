import java.io.BufferedReader;
import java.io.FileReader;
import java.util.Scanner;

public class Reader
{
	public static void main(String[] args) throws Exception
	{
		FileReader r = new FileReader(args[0]);
		BufferedReader br = new BufferedReader(r);
		String line = br.readLine();
		//System.out.print("[");
		int i = 0;
		while(line!=null)
		{
			i++;
			System.out.printf("%d\t%s%s",i,line,"\n");
			line = br.readLine();
			new Scanner(System.in).nextLine();
		}
		br.close();
		//System.out.println("]");
	}
}
