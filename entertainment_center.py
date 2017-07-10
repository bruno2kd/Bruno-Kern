import fresh_tomatoes
import media


#Here are the Movies available
toy_story = media.Movie("Toy Story", 
						"A story of a boy and his toys that come to life.", 
						"http://www.impawards.com/1995/posters/toy_story_ver1_xlg.jpg", 
						"https://www.youtube.com/watch?v=KYz2wyBy3kc")
avatar = media.Movie("Avatar", 
					"A marine on an alien planet.", 
					"http://www.impawards.com/2009/posters/avatar.jpg", 
					"https://www.youtube.com/watch?v=5PSNL1qE6VY")
lord_of_the_rings = media.Movie("Lord of the Rings", 
						"One ring to rule them all.", "http://www.impawards.com/2003/posters/lord_of_the_rings_the_return_of_the_king_xlg.jpg", "https://www.youtube.com/watch?v=V75dMMIW2B4")
fight_club = media.Movie("Fight Club", 
						"Guys make a fight club", 
						"https://s-media-cache-ak0.pinimg.com/originals/06/27/ed/0627edaeb7eda6d1659c43256f87821d.jpg", 
						"https://www.youtube.com/watch?v=SUXWAEX2jlg")
terminator = media.Movie("Terminator", 
						"Androide comes from the future to kill a future human leader.", 
						"https://s-media-cache-ak0.pinimg.com/736x/10/b2/7f/10b27fc133f7eb3a8c1751d92fd9054d.jpg", 
						"https://www.youtube.com/watch?v=k64P4l2Wmeg")
matrix = media.Movie("The Matrix", 
					"A computer hacker learns from mysterious rebels about the true nature of his reality and his role in the war against its controllers.", 
					"https://www.movieposter.com/posters/archive/main/9/A70-4902", 
					"https://www.youtube.com/watch?v=vKQi3bBA1y8")
titanic = media.Movie("Titanic", 
					"A boy and a girl from differing social backgrounds meet during the ill-fated maiden voyage of the RMS Titanic.", 
					"http://www.thereelbits.com/wp-content/uploads/2011/05/titanic-poster.jpg",
					"https://www.youtube.com/watch?v=kVrqfYjkTdQ")
la_la_land = media.Movie("La La Land", 
						"Set in modern day Los Angeles, this original musical about everyday life explores the joy and pain of pursuing your dreams.", 
						"http://www.impawards.com/2016/posters/la_la_land_ver11.jpg", 
						"https://www.youtube.com/watch?v=0pdqf4P9MB8")
the_force_awakens = media.Movie("Star Wars VII: The Force Awakens", 
								"A Star Wars Story", 
								"http://0.media.dorkly.cvcdn.com/31/28/3b0dde1d0dd0f7b1ddb491c669040502.jpg",
								"https://www.youtube.com/watch?v=sGbxmsDFVnE")

movies = [toy_story, avatar, lord_of_the_rings, fight_club, terminator, matrix, titanic, la_la_land, the_force_awakens]
fresh_tomatoes.open_movies_page(movies)
#print (media.Movie.VALID_RATINGS)

#print(media.Movie.__doc__)
#print(media.Movie.__name__)
#print(media.Movie.__module__)
