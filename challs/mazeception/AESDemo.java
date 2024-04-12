import javax.crypto.Cipher;
import javax.crypto.spec.SecretKeySpec;
import java.util.Base64;

public class AESDemo {

    public static void main(String[] args) {
        try {

            String originalText = "dctf{s0lvd_100_000_m4zs_by_h4nd}";
            String secretKey = "SecretKeyNum1337";

            byte[] plaintext = originalText.getBytes();

            for (int i = 0; i < 100000; i++) {
                plaintext = encrypt(plaintext, secretKey);
            }
            System.out.println(Base64.getEncoder().encodeToString(plaintext));


            
            for (int i = 0; i < 100000; i++) {
                plaintext = decrypt(plaintext, secretKey);
            }
            System.out.println(new String(plaintext));
            
            System.out.println("#####################################");
            String b64_res = "RVpG3DGv/wPcWVIv0RzDDPjnBZV/Nlqw8v6c1JHtEv8=";
            byte[] pes = Base64.getDecoder().decode(b64_res);
            System.out.println(new String(pes));
            for (int i = 0; i < 100000; i++) {
                pes = decrypt(pes, secretKey);
            }
            System.out.println(new String(pes));

        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    public static byte[] encrypt(byte[] plainBytes, String secretKey) throws Exception {
        Cipher cipher = Cipher.getInstance("AES/ECB/NoPadding");
        SecretKeySpec key = new SecretKeySpec(secretKey.getBytes(), "AES");
        cipher.init(Cipher.ENCRYPT_MODE, key);
        byte[] encryptedBytes = cipher.doFinal(plainBytes);
        return encryptedBytes;
    }

    public static byte[] decrypt(byte[] encryptedBytes, String secretKey) throws Exception {
        Cipher cipher = Cipher.getInstance("AES/ECB/NoPadding");
        SecretKeySpec key = new SecretKeySpec(secretKey.getBytes(), "AES");
        cipher.init(Cipher.DECRYPT_MODE, key);
        byte[] decryptedBytes = cipher.doFinal(encryptedBytes);
        return decryptedBytes;
    }
}