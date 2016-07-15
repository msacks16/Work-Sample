//Maxwell Sacks, msacks16@cmc
import java.io.*;
import java.util.*;
import org.json.JSONObject;
import org.json.JSONException;

public class Entropy {
	private static Map<String, Integer> mapper=new HashMap<String, Integer>();
	private static Integer count=0;
	public static String histogram(ArrayList<Character> slist){
		for(Character c:slist){
			String c1=Character.toString(c);
			if(mapper.containsKey(c1)){
				int previous=mapper.get(c1);
		        mapper.put(c1,previous+1);
			}
			else if(mapper.containsKey(String.format("0x%02X", (int)c))){
				int previous=mapper.get(String.format("0x%02X", (int)c));
		        mapper.put(String.format("0x%02X", (int)c),previous+1);
			}
		    else{
		    	if(((int)c)>32){
		    		mapper.put(c1,1);
		    	}
		    	else{
		    		mapper.put(String.format("0x%02X", (int)c),1);
		    	}
		    }
		 }
		 String fin="";
		 for(Map.Entry<String, Integer> entry: mapper.entrySet()){
			 fin=fin+entry.getKey()+": "+entry.getValue()+", ";
		 }
		 return "{ "+fin+" Total: "+ count+" }";
	}
	public static Double calcEntropy(Map<String, Integer> hashmap1){
		Double totEntropy=0.0;
		Iterator hashiterator=hashmap1.entrySet().iterator();
		Double newcount=(count/1.0);
		while(hashiterator.hasNext()){
			Map.Entry val= (Map.Entry) hashiterator.next();
			double val2=((int)(val.getValue())/newcount);
			totEntropy=totEntropy+val2*(Math.log(val2)/Math.log(2.0));
		}
		return totEntropy*-1;
	}
	public static void main(String[]args){
		ArrayList<Character> alist=new ArrayList<Character>();
		try{
            FileInputStream scan=new FileInputStream(args[0]);
            int byter;
    		while ((byter = scan.read()) != -1) {
    			alist.add((char)byter);
    			count=count+1;
    		}
    		scan.close();
    		System.out.println(histogram(alist));
    		System.out.println(calcEntropy(mapper));
        }
        catch (IOException e){
            e.printStackTrace();
        }
	}
}
