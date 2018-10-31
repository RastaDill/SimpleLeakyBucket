from LeakyBucket import *

if __name__ == "__main__":
	
	bucket = LeakyBucket(100, 20)
	#dirty test
	list_packgae = [10, 20, 50, 5, 8, 19, 2, 5, 7, 18, 34, 12, 25, 13]
	
	for i in list_packgae:
		bucket.leak(i)
