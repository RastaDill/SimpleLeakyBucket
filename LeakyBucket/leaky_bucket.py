#Task 3

from Queue import Queue
from threading import Thread

class LeakyBucket(object):
	def __init__(self, bucket_size, bucket_rate):
		self.BUCKET_SIZE = bucket_size #constanta
		self.buff = 0
		
		self.BUCKET_RATE = bucket_rate #constanta
		self.current_rate = bucket_rate
		
		self.queue_package = Queue()
		self.rate_thread = Thread(target = self.__start_rate)
	
	def leak(self, value):
		"""Check can output value and change self rate"""
		
		#Charge buffer(bucket)
		if self.buff + value < self.BUCKET_SIZE:
			self.buff += value
			self.queue_package.put(value)
		#When buffer is full - 
		#started sending packages under rate via Thread
		elif not self.rate_thread.isAlive():
			self.rate_thread.start()
	
	def __start_rate(self):
		while not self.queue_package.empty():
			value = self.queue_package.get() #get last value
			
			if value > self.BUCKET_RATE:
				#if package too large
				#drop him
				print "Drop\t", value
				del value
			else:
				if not self.check(value):
					print "Tact"
					self.current_rate = self.BUCKET_RATE
				
				self.current_rate -= value
				self.buff -= value
				print "Out\t", value
			
			self.queue_package.task_done()
	
	def check(self, value):
		"""Check can output value in the moment """
		
		if value <= self.current_rate:
			return True
		else:
			return False

if __name__ == "__main__":
	print "This module"

