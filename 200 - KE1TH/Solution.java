import javax.crypto.Cipher;
import javax.crypto.SecretKey;
import javax.crypto.spec.IvParameterSpec;
import javax.crypto.spec.SecretKeySpec;
import java.util.Base64;

public class Solution {

    public static String bytes_to_string(byte[] bytes)
    {
        String text = "";
        for (byte b : bytes)
        {
            text += b;

        }
        return text;
    }

    public static byte[] string_to_bytes(String string)
    {

        return null;
    }

    public static void main(String[] args)
    {
        byte[] encrypted = {-93, 35, 23, 82, -4, 57, -128, 83, -95, -60, -100, 73, 40, -86, 7, 73, -101, 3, 118, -66, -104, 69, 121, 76, 1, -124, -124, -1, -64, 29, 28, 43, 2, -25, 54, 52, -79, -62, 11, -43, 52, -72, -117, -25, -103, -55, 75, -97};
        byte[] iv = {10, -73, -33, -65, 87, 87, -121, -41, -16, 89, 12, 31, 7, 82, -43, -100};
        byte[] bkey = Base64.getDecoder().decode("/Vl4PKzS9d+Vm/0eePmaYw==");
        SecretKey key = new SecretKeySpec(bkey, 0, bkey.length, "AES");

        try
        {
            Cipher aes_cbc_pkcs5 = Cipher.getInstance("AES/CBC/PKCS5Padding");
            aes_cbc_pkcs5.init(Cipher.DECRYPT_MODE, key, new IvParameterSpec(iv));

            System.out.println(new String(aes_cbc_pkcs5.doFinal(encrypted)));
        }
        catch (Exception e)
        {
            e.printStackTrace();
        }
    }
}
