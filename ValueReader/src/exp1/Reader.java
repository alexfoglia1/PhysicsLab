package exp1;

import java.io.BufferedReader;
import java.io.FileReader;

public class Reader
{

	public static void main(String[] args) throws Exception
	{
		FileReader r = new FileReader("../exp1/values.txt");
		BufferedReader br = new BufferedReader(r);
		String line = br.readLine();
		System.out.print("[");
		while(line!=null)
		{
			System.out.print(line+",");
			line = br.readLine();
		}
		br.close();
		System.out.println("]");
	}

}
