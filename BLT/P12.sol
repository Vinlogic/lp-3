
// P12: Student Data Smart Contract

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
    function addStudent(
        uint id,
        string memory name,
        uint marks
    ) public {
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
========================================
SAMPLE INPUT / TESTING
========================================

1. Deploy the StudentData contract.

2. Add student:
   Function: addStudent()
   id: 101
   name: Rahul
   marks: 85

3. Retrieve student:
   Function: getStudent()
   index: 0

   Expected output:
   101, Rahul, 85

4. Check total students:
   Function: getCount()

   Expected output:
   1

5. Add another student:
   id: 102
   name: Priya
   marks: 90

6. Check total students again:
   Function: getCount()

   Expected output:
   2

========================================
HOW TO COMPILE AND DEPLOY
========================================

1. Open https://remix.ethereum.org

2. Create a file named P12.sol.

3. Paste this program.

4. Open Solidity Compiler.

5. Select compiler version 0.8.20 or compatible.

6. Click Compile P12.sol.

7. Open Deploy & Run Transactions.

8. Select Injected Provider - MetaMask.

9. Connect to the Sepolia test network.

10. Deploy the contract.

11. Test addStudent(), getStudent() and getCount().

========================================
IMPORTANT CONCEPTS
========================================

1. STRUCT:
   Groups related data into one custom data type.

2. ARRAY:
   Stores multiple student records.

3. PUSH():
   Adds a new student to the array.

4. MEMORY:
   Temporary data location used during function execution.

5. REQUIRE():
   Checks whether the requested array index is valid.

6. FALLBACK:
   Special function called when a contract receives
   a call with unmatched function data.
   This fallback is payable, so it can receive Ether.

========================================
GAS FEE OBSERVATION
========================================

- addStudent() changes blockchain data and costs gas.
- getStudent() and getCount() are view functions.
- Reading them through Remix does not require an
  on-chain transaction fee.
- Gas fee = Gas used × Effective gas price.

========================================
*/
