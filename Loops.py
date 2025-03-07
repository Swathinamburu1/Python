#1. Write a program to print “Bright IT Career” ten times using for loop.

      a = "Bright IT Career"
      for i in range(10):
          print(a)

#2. Write a program to print 1 to 20 numbers using the while loop.

      i = 1
      while(i<=20):
          print(i)
          i+= 1 
  
#3. Program to equal operator and not equal operators.

      a = 5
      b = 10
      print(a ==b) # Equal operator
      print(a != b) # Not Equal operator

#4. Write a program to print the odd and even numbers.

      numbers = [1,2,3,4,5,6,7,8,9,10]
      print("Even Numbers: ")  
      for i in numbers:     
          if i % 2 == 0:       
              print(i, end =" ")    
      print("\nOdd Numbers:")
      for i in numbers:
          if i % 2 != 0:
              print(i, end =" ")

#5. Write a program to print largest number among three numbers.

      k = 240
      a = 250
      s = 290
      if k >= a and k >= s:
          largest = k
      elif a >= k and a >= s:
          largest = a
      else:
          largest = s
      print("Largest number is: ",largest)  

#6. Write a program to print even number between 10 and 20 using while.

      a = 10
      b = 20
      print("Even Numbers Between 10 to 20: ",end=" ")
      while a <= b:
          if(a % 2 == 0):
              print("{0}".format(a),end=" ")
          a = a + 1

#7. Write a program to print 1 to 10 using the do-while loop statement.

      a = 1
      print("Print 1 to 10 using the do-while loop statement:",end=" ")
      while True:
          print(a,end=" ")
          a = a + 1
          if(a > 10):
              break 

#8. Write a program to find Armstrong number or not.

      a = int(input('Enter a number to check if its armstrong or not: '))
      sum = 0
      temp = 0
      temp = a
      while temp > 0:
          r = temp % 10
          sum += r ** 3
          temp //= 10
      if a == sum:
          print(a," is an amstrong number")
      else:
          print(a," is not an amstrong number")

#9. Write a program to find the prime or not.

      number = int(input("Enter any number to check prime number or not: "))
      if number > 1:
          for i in range(2, number):
              if (number % i) == 0:
                  print(number, "is not a prime number")
                  break
          else:
              print(number, "is a prime number")
      else:
          print(number, "is not a prime number")

#10. Write a program to palindrome or not.

      n = int(input("Enter number to check palindrome or not:"))
      temp = n
      rev = 0
      while(n > 0):
          dig = n % 10
          rev = rev * 10 + dig
          n = n // 10
      if(temp == rev):
          print("The number is a palindrome!")
      else:
          print("The number isn't a palindrome!") 

#11. Program to check whether a number is EVEN or ODD.

      # Python program to check whether a number is EVEN or ODD using a switch-like approach
      def check_even_odd(n):
          switch = {
              0: "Even",
              1: "Odd"
          } 
          # Using modulus to determine even or odd
          result = switch[n % 2]
          return result
      # Taking user input
      num = int(input("Enter Number to check is EVEN or ODD: "))
      print(f"The number {num} is {check_even_odd(num)}.")


#12. Python program to print gender based on input M/F using a switch-like approach

      def get_gender(char):
          switch = {
              'M': "Male",
              'F': "Female"
          }
          # Using get() to handle invalid inputs gracefully
          return switch.get(char.upper(), "Invalid Input")
      # Taking user input
      gender_char = input("Enter M or F: ")
      print(f"Gender: {get_gender(gender_char)}")
