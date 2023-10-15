// #1

const instance1 = {
    name: "singleton"
}

const instance2 = {
    name: "singleton"
}

// console.log(instance1 === instance2); // false
// console.log({} === {}); // false

// #2
//// #bad

// let instance;

// class Counter {
//     constructor() {
//         if (!instance) instance = this;
//         instance.count = 0;
//         return instance;
//     }

//     getCount() {
//         return instance.count;
//     }

//     increaseCount() {
//         return instance.count++;
//     }
// }

//// #good
class Counter {
    constructor() {
        if (typeof Counter.instance === 'object')  {
            return Counter.instance;
        }

        // console.log(this);
        
        this.count = 0;
        Counter.instance = this;
        return this;
    }

    getCount() {
        return this.count;
    }

    increaseCount() {
        return this.count++;
    }
}

// ----
const myCount1 = new Counter();
const myCount2 = new Counter();

myCount1.increaseCount();
myCount1.increaseCount();
myCount2.increaseCount();
myCount2.increaseCount();

console.log(myCount2.getCount()); // 4
console.log(myCount1.getCount()); // 4

