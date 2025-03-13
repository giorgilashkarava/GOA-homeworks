# შექმენით tuple, რომელიც შეიცავს თქვენს 5 საყვარელ ფილმს, შემდეგ კი დაბეჭდეთ პირველი და ბოლო ელემენტი ამ tuple-დან.
film = tuple(" forsaji, the hauntingof hill house, haloween, the friday 13 th, central intelligence ")
(first, *second,) = film
print(first)
print(second)