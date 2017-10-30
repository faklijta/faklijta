const Panama = {
    cash: 0,
    name: 'Panama',
    tax: '1%',
    deposit: function(amt) {
        this.cash += 1000;
        console.log('Panama got ' + this.cash)
    }
}
const Cyprus = {
    cash: 0,
    name: 'Cyprus',
    tax: '5%',
    deposit: function(amt) {
        this.cash += 1000;
        console.log('Cyprus got ' + this.cash)
    }
}
const Shuffler = {
    cash: 10000,
    transactionCount : 0,
    pick: function() {
        if (this.transactionCount % 2 === 0) {
            Panama.deposit(1000)
        } else {
            Cyprus.deposit(1000)
        }
        this.transactionCount++;
    }
}

Shuffler.pick() // prints Panama got 1000
Shuffler.pick() // prints Cyprus got 1000
Shuffler.pick() // prints Panama got 1000
Shuffler.pick() // prints Cyprus got 1000

console.log( Panama.cash ) // 2000 
console.log( Cyprus.cash ) // 2000 