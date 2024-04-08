using System.Security.Cryptography;

Console.Write("Enter the flag: ");
var input = Console.ReadLine();

var iv = Convert.FromBase64String("AP+Xw0XhvDqW/CclMQj+yA==");
var key = Convert.FromBase64String("2sh0c1dmFK83JbHep6wL6wvIz/402a18yH53K6HZ4x0=");
var ct = Convert.FromBase64String("mqJYU0V4INdXJzmn+WTVMr6fV9ButWkYm+F1XKQeeVNjSsGpMXOTbCblRBGPV8Ba");

var aes = Aes.Create();
aes.IV = iv;
aes.Key = key;
using MemoryStream streamCt = new();
{
    var encryptor = aes.CreateEncryptor();
    using CryptoStream cs = new(streamCt, encryptor, CryptoStreamMode.Write);
    using StreamWriter sw = new(cs);
    sw.Write(input);
}

Console.WriteLine(Enumerable.SequenceEqual(ct, streamCt.ToArray()) ? "Correct!" : "Try again");
