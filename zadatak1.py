from test_module import Test

# ako neces da gledas posebne testove, vec samo krajnji rezultat testiranja funkcije, stavi ovo na False
DEBUG = True

def min_function(niz):
	# racuna minimalan element niza
	# preporucuje se izbegavanje funkcije min radi vezbanja
	return None

def max_function(niz):
	# racuna maksimalan element niza
	# preporucuje se izbegavanje funkcije max radi vezbanja
	return None

def len_function(niz):
	# racuna duzinu niza
	# preporucuje se izbegavanje funkcije len radi vezbanja
	return None

def sum_function(niz):
	# racuna sumu elemenata niza
	# preporucuje se izbegavanje funkcije sum radi vezbanja
	return None

if __name__ == "__main__":
	Test(min_function, more_info=DEBUG).run_multiple_tests([
		([1, 2, 3], 1),
		([3, 4, 5], 3),
		([16, 32, 17], 16)
	])