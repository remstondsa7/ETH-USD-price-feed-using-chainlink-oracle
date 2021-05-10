from web3 import Web3

kovan_url='https://kovan.infura.io/v3/96e3a3cebe314349806698733adc4ab7'
web3 = Web3(Web3.HTTPProvider(kovan_url))
abi='''[
	{
		"inputs": [],
		"name": "decimals",
		"outputs": [
			{
				"internalType": "uint8",
				"name": "",
				"type": "uint8"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "description",
		"outputs": [
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint80",
				"name": "_roundId",
				"type": "uint80"
			}
		],
		"name": "getRoundData",
		"outputs": [
			{
				"internalType": "uint80",
				"name": "roundId",
				"type": "uint80"
			},
			{
				"internalType": "int256",
				"name": "answer",
				"type": "int256"
			},
			{
				"internalType": "uint256",
				"name": "startedAt",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "updatedAt",
				"type": "uint256"
			},
			{
				"internalType": "uint80",
				"name": "answeredInRound",
				"type": "uint80"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "latestRoundData",
		"outputs": [
			{
				"internalType": "uint80",
				"name": "roundId",
				"type": "uint80"
			},
			{
				"internalType": "int256",
				"name": "answer",
				"type": "int256"
			},
			{
				"internalType": "uint256",
				"name": "startedAt",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "updatedAt",
				"type": "uint256"
			},
			{
				"internalType": "uint80",
				"name": "answeredInRound",
				"type": "uint80"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "version",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	}
]'''

addr = '0x9326BFA02ADD2366b30bacB125260Af641031331'
contract = web3.eth.contract(address=addr, abi=abi)

record={}

def get_latest_ETH_price():
    latest_ETH_price = contract.functions.latestRoundData().call()
    return latest_ETH_price[1]/10**8

def record_ETH_prices():
    new_ETH_price=get_latest_ETH_price()
    idx=len(record)
    record[idx]=new_ETH_price
    idx=idx+1
    return True
    
def calculate_mean_of_ETH_price():
    n=len(record)
    if n==0:
        return 0.0
    return sum(record.values())/n

def update_record(id):
    n=len(record)
    if id<n:
        record[id]=get_latest_ETH_price()
        return True
    return False

def delete_record(id):
    n=len(record)
    if id in record.keys():
        del record[id]
        return True
    return False

def display_record():
    for id,price in record.items():
        print("{}: {}".format(id,price))

def menu(option):
   
    if option==1:
        price=get_latest_ETH_price()
        print('The Latest Price of ETH/USD is: ',price)
        
    elif option==2:
        if record_ETH_prices():
            print('The Latest ETH/USD price SUCCESSFULLY recorded: ')
        
    elif option==3:
        mean=calculate_mean_of_ETH_price()
        if mean==0:
            print('==== ETH/USD prices NOT recorded ==== ')
        else:
            print('The mean of ETH/USD prices is :',mean)     
        
    elif option==4:
        id=int(input('Enter the Record ID to be updated:\n'))
        if update_record(id):
            print('ETH/USD price successfully updated for Id {}: '.format(id))
        else:
            print('ID Does NOT Exists')
        
    elif option==5:
        id=int(input('Enter the Record ID to be Deleted:\n'))
        if delete_record(id):
            print('ETH/USD price successfully deleted for Id {}: '.format(id))
        else:
            print('ID {} Does NOT Exists'.format(id))
            
    elif option==6:
        display_record()
        
    elif option==7:
        pass
    
    else:
        print('############Option not Recognized############\n')
        menu()
    
if __name__=='__main__':
    
    option=-1
    while option!=7:
        option=int(input('''
Enter the choice:
1. Get Latest ETH/USD price
2. Record New ETH/USD prices
3. Calculate Mean of the recorded ETH/USD prices
4. Update the Record
5. Delete the Record
6. Display Record
7. Exit
'''))
        menu(option)
    print('*******THANK YOU********')
    
    
        

