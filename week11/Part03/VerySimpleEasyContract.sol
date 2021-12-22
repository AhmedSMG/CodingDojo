// SPDX-License-Identifier: GPL-3.0
pragma solidity ^0.8.0;

contract EasiestContract{

    string private secret;

    constructor(){
        secret = "Unknown";
    }

    function setSecret(string memory _message) external{
        secret = _message;
    }

    function getSecret() external view returns(string memory){
        return secret;
    }

}