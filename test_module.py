import sys
import string

assert sys.version_info >= (3,0)

class Test:
	def __init__(self, function, more_info=True):
		self.function = function
		self.number_of_tests = 0
		self.successful_tests = 0
		self.more_info = more_info

	def reset(self):
		self.number_of_tests = 0
		self.successful_tests = 0

	def run(self, *input_value, expected_value):
		if len(input_value) == 1:
			input_value = input_value[0]
		self.number_of_tests += 1
		if self.more_info:
			print(' [' + self.function.__name__ + '] Test ' + str(self.number_of_tests) + ': ', end='')
		try:
			result = self.function(input_value)
			if(result == expected_value):
				if self.more_info:
					print('successful')
				self.successful_tests += 1
			else:
				if self.more_info:
					print('failed (Expected value is ' + str(expected_value) + ', but function result is ' + str(result))
		except:
			if self.more_info:
				print('failed (Functon failed during execution)')

	def info(self):
		print('Testing of function "%s" ' % self.function.__name__, end='')
		if self.number_of_tests == self.successful_tests:
			print('succeeded')
		else:
			print('failed, %d out of %d tests passed' % (self.successful_tests, self.number_of_tests))
		print('')

	def run_multiple_tests(self, tests):
		self.reset()
		for i in tests:
			self.run(i[0], expected_value=i[1])
		self.info()

class SolutionGenerator:
	@staticmethod
	def generate(function, print_format, samples):
		output = ''
		for i in samples:
			#try:
			result = function(i)
			output += string.replace(print_format, '%in%', i).replace('%out%', result)
			#except:
			#	pass
		return output