// SPDX-License-Identifier: GPL-3.0

pragma solidity ^0.8.0;

// interface IERC20 {

//     function totalSupply() external view returns (uint256);
//     function balanceOf(address account) external view returns (uint256);
//     function transfer(address recipient, uint256 amount) external returns (bool);
//     function allowance(address owner, address spender) external view returns (uint256);
//     function approve(address spender, address recipient, uint256 amount) external returns (bool);
//     function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);

//     event Transfer(address indexed from, address indexed to, uint256 value);
//     event Approval(address indexed owner, address indexed spender, uint256 value);
// }

import "https://raw.githubusercontent.com/OpenZeppelin/openzeppelin-contracts/master/contracts/token/ERC20/ERC20.sol";

contract MyToken is ERC20 {
    constructor(string memory name, string memory symbol) ERC20(name, symbol) public {
        _mint(msg.sender, 10**20);
    }

    function giveMeTokens(uint token_count) public {
        _mint(msg.sender, token_count * (10**18));
    }

    function buy_token() public payable{
        _mint(msg.sender, msg.value);
    }

    function sell_token(uint amount) public payable{
        _burn(msg.sender, amount);
        payable(msg.sender).transfer(amount);
    }
}