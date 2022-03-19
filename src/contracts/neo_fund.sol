// SPDX-License-Identifier: MIT

pragma solidity ^0.7;

contract NeoFund {
    address public owner;

    // complete log of all of funders
    address[] public funders;

    // map funders to the amount that they funded
    mapping(address => FundedAmount) public funders_amount;

    constructor() {
        owner = msg.sender;
    }

    struct FundedAmount {
        uint256 amount;
        bool exists;
    }

    modifier onlyAdmin() {
        require(
            msg.sender == owner,
            "Only admin can withdraw from the contract."
        );
        _;
    }

    function get_contract_balance() public view returns (uint256) {
        return address(this).balance;
    }

    function fund() public payable {
        if (funders_amount[msg.sender].exists) {
            funders_amount[msg.sender].amount += msg.value;
        } else {
            funders_amount[msg.sender] = FundedAmount({
                amount: msg.value,
                exists: true
            });
            funders.push(msg.sender);
        }
    }

    function withdraw(uint256 withdraw_amount) public payable onlyAdmin {
        require(
            withdraw_amount <= address(this).balance,
            "Amount to withdraw is greater than the actual balance."
        );

        uint256 collected_amount = 0;
        uint16 i = 0;
        uint256 funder_withdrawing_amount = 0;
        // update funders fudned amounts records
        while (collected_amount < withdraw_amount || i > funders.length) {
            address funder = funders[i];
            uint256 fund_remaining_amount = funders_amount[funder].amount;

            if (fund_remaining_amount == 0) {
                continue;
            }

            if (collected_amount + fund_remaining_amount > withdraw_amount) {
                funder_withdrawing_amount = withdraw_amount - collected_amount; // only the required amount
            } else {
                funder_withdrawing_amount = funders_amount[funder].amount; // all of the amount that the funder funded
            }
            collected_amount += funder_withdrawing_amount;
            funders_amount[funder].amount -= funder_withdrawing_amount;

            i++;
        }
        payable(msg.sender).transfer(withdraw_amount);
    }
}
