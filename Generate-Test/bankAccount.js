class BankAccount {
  constructor(accountHolder, accountNumber, initialBalance = 0) {
    this.accountHolder = accountHolder;
    this.accountNumber = accountNumber;
    this.balance = initialBalance;
  }

  deposit(amount) {
    if (amount > 0) {
      this.balance += amount;
      console.log(`Deposited $${amount}. New balance: $${this.balance}`);
    } else {
      console.log("Invalid deposit amount. Amount must be greater than 0.");
    }
  }

  withdraw(amount) {
    if (0 < amount && amount <= this.balance) {
      this.balance -= amount;
      console.log(`Withdrew $${amount}. New balance: $${this.balance}`);
    } else if (amount > this.balance) {
      console.log("Insufficient funds for withdrawal.");
    } else {
      console.log("Invalid withdrawal amount. Amount must be greater than 0.");
    }
  }

  getBalance() {
    console.log(`Account balance for ${this.accountHolder}: $${this.balance}`);
  }

  toString() {
    return `Account Holder: ${this.accountHolder}\nAccount Number: ${this.accountNumber}\nBalance: $${this.balance}`;
  }
}

