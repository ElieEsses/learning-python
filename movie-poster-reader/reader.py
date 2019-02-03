from pytesseract import image_to_string
from PIL import Image
import imdb

image = Image.open(input("Please type in a file name. "))	
image = image.convert("L")									
movie_string = image_to_string(image)	

ia = imdb.IMDb()
s_result = ia.search_movie(movie_string)
movie = s_result[0]
ia.update(movie)		

plot = movie["plot"][0]		
head, sep, tail = plot.partition('.::')							
plot = head
					
director = movie["director"][0]

cast = movie["cast"]

print("Title: " + str(movie))
print("Plot: " + str(plot))
print("Director: " + str(director))
print("Actors: ")	
for people in range(0,4):							
	print(cast[people])