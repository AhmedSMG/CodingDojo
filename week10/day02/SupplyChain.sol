// SPDX-License-Identifier: GPL-3.0

pragma solidity ^0.8.0;


contract SupplyChain{

    address private owner;
    uint256 private idCounter = 0;


    constructor(){
        owner = msg.sender;
    }


    struct Asset{
        uint256 id;
        string name;
        address buyer;
        address seller;
        uint256 price;
        uint state; // 0 NOT There,
                    // 1 For Sale,
                    // 2 Sold,
                    // 3 Shipped,
                    // 4 Recived,

                    // 5 Confirm Recived, finlized

                    // 6 Reject Recived,

                    // 7 Refund,
                    // 8 Dispute,
    }

    mapping (uint256 => Asset) assets;

    function addAsset(string memory _name, uint256 _price) external returns (uint256){
        idCounter += 1;
        assets[idCounter] = Asset({id: idCounter,
                                   name: _name,
                                   buyer: address(0),
                                   seller: msg.sender,
                                   price: _price,
                                   state: 1 // For Sale
                                   });
        return idCounter;
    }

    function buyAsset(uint256 _id) external payable{
        require(assets[_id].state == 1, "Asset not for sale"); // Make sure asset for sale
        require(assets[_id].price <= msg.value, "No sufficient fund!");
        assets[_id].buyer = msg.sender;
        assets[_id].state = 2; // Sold
        uint256 refunds = msg.value - assets[_id].price;

        if (refunds > 0){
            payable(msg.sender).transfer(refunds);
        }
    }

    function shipAsset(uint256 _id) external{
        require(assets[_id].state == 2); // make sure asset Sold
        require(assets[_id].seller == msg.sender); // Shipping for seller only
        assets[_id].state = 3; //Shipped
    }


    function reciveAsset(uint256 _id) external{
        require(assets[_id].state == 3); // make sure asset Shipped
        require(assets[_id].buyer == msg.sender); // Recived for Buyer only
        assets[_id].state = 4; // Recived
    }

    function confirm(uint256 _id) external{
        require(assets[_id].state == 4); // make sure asset Recived
        require(assets[_id].buyer == msg.sender); // Confirmation for Buyer only
        assets[_id].state = 5; // Confirmiation
        payable(assets[_id].seller).transfer(assets[_id].price);
    }

    function reject(uint256 _id) external{
        require(assets[_id].state == 4); // make sure asset Recived
        require(assets[_id].buyer == msg.sender); // Confirmation for Buyer only
        assets[_id].state = 6; // Rejection
    }

    function refund(uint256 _id) external{
        require(assets[_id].state == 6); // make sure asset Recived
        require(assets[_id].seller == msg.sender); // Refund for Seller only
        payable(assets[_id].buyer).transfer(assets[_id].price);
        assets[_id].buyer = address(0); // reset
        assets[_id].state = 1; // reset

    }

    function dispute(uint256 _id) external{
        require(assets[_id].state == 6); // make sure asset Recived
        require(assets[_id].seller == msg.sender); // Refund for Seller only
        assets[_id].state = 8;
    }

   function fetchAsset(uint256 _id) external view returns (uint256,
                                                           string memory,
                                                           uint256,
                                                           uint,
                                                           address,
                                                           address) {
       
       return (assets[_id].id,
               assets[_id].name,
               assets[_id].price,
               assets[_id].state,
               assets[_id].seller,
               assets[_id].buyer);
   }





}