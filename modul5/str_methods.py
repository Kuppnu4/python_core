def main():
   a = ["hello", "world", "buy"]
   delim = ","

   decoded_list = delim.join(a)

   print(decoded_list)

   b = decoded_list.split(delim)
   print(b)
        
if __name__ == "__main__":
     main()
