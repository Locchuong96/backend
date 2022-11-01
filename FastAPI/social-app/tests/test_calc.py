import pytest
from app.calculations  import add,subtract,multiply,divide,BankAccount,InsufficientFunds

# DEFINE TEST FUNCTION

@pytest.fixture
def zero_bank_account():
	return BankAccount()

@pytest.fixture
def bank_account():
	return BankAccount(50)

@pytest.mark.parametrize("num1,num2,out",[
	(3,2,5), # testcase1
	(7,1,8), # testcase2
	(2,2,4) # testcase3
	])
def test_add(num1,num2,out):
	'''
	the test pass if using this function without any error
	the naming must be test_* some
	'''
	print('testing add function')
	assert out == add(num1,num2)

@pytest.mark.parametrize("num1,num2,out",[
	(3,2,1), # testcase1
	(7,1,6), # testcase2
	(2,2,0) # testcase3
	])
def test_subtract(num1,num2,out):
	print('testing subtract function')
	assert out == subtract(num1,num2)

def test_multiply():
	print('testing multiply function')
	out = multiply(5,3)
	assert 15 == out

def test_divide():
	print('testing divide function')
	out = divide(5,3)
	assert 5/3 == out

@pytest.mark.parametrize("starting_balance",[
	(20),
	(10)
	])
def test_bank_set_initial_amount(starting_balance):
	print('testing set initial amount')
	bank_account = BankAccount(starting_balance)
	assert bank_account.balance == starting_balance

def test_bank_default_amount(zero_bank_account):
	# bank_account = BankAccount()
	print('testing default amount')
	assert zero_bank_account.balance == 0

@pytest.mark.parametrize("starting_balance,amount,balance",[
	(20,10,10),
	(10,10,10),
	(30,40,-10)
	])
def test_bank_withdraw(starting_balance,amount,balance):
	print('testing bank withdraw')
	bank_account = BankAccount(starting_balance)
	bank_account.withdraw(amount)
	assert bank_account.balance == starting_balance - amount

@pytest.mark.parametrize("starting_balance,amount,balance",[
	(20,10,30),
	(10,10,20),
	(30,40,70)
	])
def test_bank_deposit(starting_balance,amount,balance):
	print('testing bank deposit')
	bank_account = BankAccount(starting_balance)
	bank_account.deposit(amount)
	assert bank_account.balance == starting_balance + amount

def test_collect_interest(bank_account):
	print('testing collect interest')
	bank_account.collect_interest()
	assert bank_account.balance == 50 * 1.1

@pytest.mark.parametrize("deposit,withdraw,balance",[
	(200,150,50),
	(500,400,100),
	(300,400,-100)
	])
def test_bank_transaction(zero_bank_account,deposit,withdraw,balance):
	print('testing bank transaction')
	zero_bank_account.deposit(deposit)
	zero_bank_account.withdraw(withdraw)
	assert zero_bank_account.balance == balance

def test_insufficient_funds(bank_account):
	with pytest.raises(InsufficientFunds): #define the exception
		bank_account.withdraw(200)

# RUN TEST FUNCTION

if __name__ == "__main__":
	
	test_add()

	test_subtract()

	test_multiply()

	test_divide()

	# we do not have to declare the function for testing with pytest
