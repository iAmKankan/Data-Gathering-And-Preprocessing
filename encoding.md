### What are encodings?
 ![Light](https://user-images.githubusercontent.com/12748752/126914730-b5b13ba9-4d20-4ebf-b0ed-231af4c8b984.png)

* Character encodings are specific sets of rules for mapping from raw binary byte strings (that look like this: 0110100001101001) to characters that make up human-readable text (like "hi").
* There are many different encodings, and if you tried to read in text with a different encoding than the one it was originally written in, you ended up with scrambled text called ["mojibake" (said like mo-gee-bah-kay).](https://en.wikipedia.org/wiki/Covariance_and_correlation)
* There are lots of different character encodings, but the main one you need to know is UTF-8.
*   UTF-8 is the standard text encoding. All Python code is in UTF-8 and, ideally, all your data should be as well. It's when things aren't in UTF-8 that you run into trouble.
* There are two main data types you'll encounter when working with text in Python 3. 
  *  **One is is the string, which is what text is by default.**
  *  **The other data is the bytes data type, which is a sequence of integers.**
*  You can convert a string into bytes by specifying which encoding it's in:


