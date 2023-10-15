// #1 
class TeslaCar {
    constructor(model, price, interior, autopilot) {
        this.model = model;
        this.price = price;
        this.interior = interior;
        this.autopilot = autopilot;
    }

    produce() {
        return new TeslaCar(this.model, this.price, this.interior, this.autopilot);
    }
}

// ---
// produce base auto
const prototypeCar = new TeslaCar('S', 80000, 'black', false);

// cloning of base auto
const car1 = prototypeCar.produce();
const car2 = prototypeCar.produce();
const car3 = prototypeCar.produce();

// change for particular auto
car1.interior = "white";
car1.autopilot = true;

//


// #2 вариант в комментах 
// на мой взгляд лучше
class TeslaCar {
    constructor(model, price, interior, autopilot) {
      this.model = model;
      this.price = price;
      this.interior = interior;
      this.autopilot = autopilot;
    }
  }
  
  function produceFromPrototype(prototypeCar) {
    const { model, price, interior, autopilot } = prototypeCar;
    return new TeslaCar(model, price, interior, autopilot);
  }
  
  
  const prototypeCar = new TeslaCar("S", 80000, "black", false);
  
  const car1 = produceFromPrototype(prototypeCar);
  const car2 = produceFromPrototype(prototypeCar);
  const car3 = produceFromPrototype(prototypeCar);
  
  car1.interior = "white";
  car1.autopilot = true;
  
  console.log(car1);
  console.log(car2);
  console.log(car3);
  
  /*
    И вообще напрямую менять свойства объекта некомильфо, лучше сделать что-то этого:
    const car = produceFromPrototype(prototypeCar, { interior: "white", autopilot: true });
  */
  