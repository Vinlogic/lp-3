// P15: Student Data Smart Contract

// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract StudentData {

    // Structure to store student information
    struct Student {
        uint id;
        string name;
        uint marks;
    }

    // Array to store multiple students
    Student[] public students;

    // Add a new student
    function addStudent(uint id, string memory name, uint marks) public {
        students.push(Student(id, name, marks));
    }

    // Retrieve student details using array index
    function getStudent(uint index)
        public
        view
        returns (uint, string memory, uint)
    {
        require(index < students.length, "Invalid index");

        Student memory s = students[index];

        return (s.id, s.name, s.marks);
    }

    // Return total number of students
    function getCount() public view returns (uint) {
        return students.length;
    }

    // Fallback function
    fallback() external payable {
    }
}

/*
SAMPLE TESTING:

1. Deploy the StudentData contract.

2. Call addStudent():
   id: 101
   name: Rahul
   marks: 85

3. Call getStudent() with index 0.

Expected output:
101, Rahul, 85

4. Call getCount().

Expected output:
1

5. Add another student:
   id: 102
   name: Priya
   marks: 90

6. Call getCount() again.

Expected output:
2

HOW TO COMPILE AND DEPLOY:

1. Open https://remix.ethereum.org
2. Create a file named P12.sol.
3. Paste this program.
4. Select Solidity compiler 0.8.20.
5. Compile P12.sol.
6. Open Deploy & Run Transactions.
7. Select Injected Provider - MetaMask.
8. Connect to Sepolia test network.
9. Deploy the contract.
10. Test addStudent(), getStudent() and getCount().

FALLBACK TEST:

Send a small amount of test ETH directly to the contract
without selecting a function. This calls the payable fallback
when the call data does not match a function (and no receive
function is defined).

IMPORTANT CONCEPTS:

1. STRUCT: Groups related data into one custom data type.
2. ARRAY: Stores multiple student records.
3. PUSH(): Adds a new student to the array.
4. MEMORY: Temporary data location.
5. REQUIRE(): Checks whether the array index is valid.
6. FALLBACK: Handles calls with unmatched function data.

GAS FEE OBSERVATION:

- addStudent() changes blockchain data and costs gas.
- getStudent() and getCount() are view functions.
- Normal Remix read calls do not require an on-chain fee.
- Gas fee = Gas used x Effective gas price.
*/
