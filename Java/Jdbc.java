//package clapackage;
import java.sql.*;
//import clapackage.*;
public class Jdbc
{
  public static void main(String[] args)
  {
	  
    try
    {
      String url="jdbc:mysql://localhost/test";
      String user="root";
      String pwd="";
      
      //������������һ��Ҳ��дΪ��Class.forName("com.mysql.jdbc.Driver");
     Class.forName("com.mysql.jdbc.Driver").newInstance();
//    Class.forName( "org.gjt.mm.mysql.Driver").newInstance();
      //������MySQL������
       Connection conn = DriverManager.getConnection(url,user, pwd);
      
      //ִ��SQL���
       Statement stmt = conn.createStatement();//��������������ִ��sql����

//	 System.out.println(args);
//      ResultSet rs = stmt.executeQuery(args);
    
      ResultSet rs = stmt.executeQuery( "select * from user" );
       //��������
      while (rs.next())
      {
        String name = rs.getString("name");
        System.out.println(name);
      }
      
      rs.close();//�ر����ݿ�
      conn.close();
    }
    catch (Exception ex)
    {
      System.out.println("Error : " + ex.toString());
    }
  }
}
