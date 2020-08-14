#!/usr/bin/python3
#Created by KIRILL SHVEDOV

'''BREADTH SEARCH
THIS ALGORITHM HELPS YOU 
TO DEFINE 
THE WAY/'S LENGTH FROM A TO B'''

from collections import deque 


def person_is_seller(name):
	return name[-1] == 'o'

def search(name):
	search_queue = deque()
	search_queue += graph["me"]
	searched = []
	while search_queue:
		person = search_queue.popleft()
		if not person in searched:
			if person_is_seller(person):
				return person + " is a mango seller!" 
			else:
				search_queue += graph[person]
				searched.append(person)
	return False





graph = {}
graph["me"] = ["Gnida", "Mraz", "Sidor\'o"]
graph["Gnida"] = ["Shamil","Sosunok","Gondonio"]
graph["Mraz"] = ["Dnische"]
graph["Sidor\'o"] = []

print(search("me"))

