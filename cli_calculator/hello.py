# task 1
book = {
    "Title": "Half of a Yellow Sun", "Author": "Chimamanda Ngozi Adichie", "Price": 20.00

}

print(book["Author"])

# task 2
book2 = {

     "Title": "Things Fall Apart", 
     "Author": "Chinua Achebe",
     "Price": 15.00
}

# task 3

books = [
     { "Title": "Half of a Yellow Sun", "Author": "Chimamanda Ngozi Adichie", "Price": 20.00},
     {  "Title": "Things Fall Apart", "Author": "Chinua Achebe", "Price": 15.00}
]

# task 4
#  numbers = [10, 20]
#  numbers.append(30)

#print(numbers)

book3 = {
      "Title": "Python Crash Course",
       "Author": "Eric Matthes",
        "Price": 25.00
}
books.append(book3)
print(books)

# task 5
# Calculate the total price of all three books
total = 0

books.append({
    "Title": "Atomic Habits",
    "Author": "James Clear",
    "Price": 30.0
})
for book in books:
     print(book["Title"], "Cost", book["Price"])    
     total += book["Price"]
print(len(books))
print(total)
