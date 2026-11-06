
// P11: Bank Account Smart Contract

// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract BankAccount {

    // Stores the balance of each user's wallet address
    mapping(address => uint) public balance;

    // Deposit Ether into the user's account
    function deposit() public payable {
        require(msg.value > 0, "Amount must be greater than zero");

        balance[msg.sender] += msg.value;
    }

    // Withdraw Ether from the user's account
    function withdraw(uint amount) public {
        require(amount > 0, "Amount must be greater than zero");
        require(balance[msg.sender] >= amount, "Insufficient balance");

        // Update balance before sending Ether
        balance[msg.sender] -= amount;

        // Transfer Ether to the user's wallet
        (bool success, ) = payable(msg.sender).call{value: amount}("");

        require(success, "Transfer failed");
    }

    // Display the user's account balance
    function showBalance() public view returns (uint) {
        return balance[msg.sender];
    }
}

/*
========================================
SAMPLE INPUT / TESTING
========================================

1. Deploy the BankAccount contract.

2. Deposit:
   Value: 1
   Unit: Ether
   Function: deposit()

3. Check balance:
   Function: showBalance()

   Expected output:
   1000000000000000000 wei

4. Withdraw:
   Amount: 200000000000000000
   Function: withdraw()

5. Check balance again:
   Function: showBalance()

   Expected output:
   800000000000000000 wei

========================================
HOW TO COMPILE AND RUN
========================================

1. Open https://remix.ethereum.org

2. Create a file named P11.sol.

3. Paste this program.

4. Open the Solidity Compiler.
   Select compiler version 0.8.20 or compatible.

5. Click Compile P11.sol.

6. Open Deploy & Run Transactions.

7. Select Injected Provider - MetaMask.

8. Connect MetaMask using the Sepolia test network.

9. Deploy the contract.

10. Test deposit(), withdraw() and showBalance().

IMPORTANT:
- Use test ETH only.
- Never share your wallet password or seed phrase.
- Transaction fees (gas fees) are paid for state-changing
  transactions such as deposit() and withdraw().
- showBalance() is a read-only function.

========================================
*/
