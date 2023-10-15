// #1

class Bmw {
    constructor(model, price, maxSpeed) {
        this.model = model;
        this.price = price;
        this.maxSpeed = maxSpeed;
    }
};

class BmwFactory {
    create(type) {
        if (type === 'x5') {
            return new Bmw(type, 108000, 300);
        }

        if (type === 'x6') {
            return new Bmw(type, 111000, 400);
        }
    }
};

const factory = new BmwFactory();

const x5 = factory.create('x5');
const x6 = factory.create('x6');