pragma solidity ^0.6.0;

/*
    chainlink Oracle
    
*/

import "https://github.com/smartcontractkit/chainlink/blob/master/evm-contracts/src/v0.6/interfaces/AggregatorV3Interface.sol";

contract price_feed{
    
    AggregatorV3Interface internal priceFeed;
    

    constructor() public{
        /*
            Kovan Network:'0x9326BFA02ADD2366b30bacB125260Af641031331'
        */
        priceFeed=AggregatorV3Interface(0x9326BFA02ADD2366b30bacB125260Af641031331);
    }
    
    
    struct Data{
        /*
            struct Data Structure
        */
        int price;
        
    }
    
    mapping(int => Data) map_data;
    int internal id=0;
    
   
    
    function getLatestPrice() public view returns (int){
         /*
            Fetches Current ETH/USD prich from chainlink Oracle
        */
        
        (
            uint80 roundID, 
            int price,
            uint startedAt,
            uint timeStamp,
            uint80 answeredInRound
        ) = priceFeed.latestRoundData();
        
        return price;
        
    }
    
    /*
        Function to calculate mean of the prices stored
    */
    
    function calculate_mean() public view returns(int){
        int sum=0;
        
        for(int i =0; i<=id; i++){
            
            sum=sum+map_data[i].price;
            
        }
        
        int avg=sum/(id);
        return avg;
        
    }
    
    /*
        CRUD operations
    */
    
    function record_ETHprice_data() public{
        /*
            Record Data in struct
        */
        
        int _price=getLatestPrice();
        map_data[id].price=_price;
        id=id+1;
        
    }
    
    
    function read_ETHprice_data(int id) public view returns(int){
        
        return map_data[id].price;
        
    }
    
    function update_ETHprice_data(int id) public returns(int){
        
        map_data[id].price=getLatestPrice();
        
    }
    
    function delete_ETHprice_data(int id) public returns(int){
        
        delete map_data[id].price;
        
    }
    
}
    
    
    
