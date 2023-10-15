class Engine2 {
    simpleInterface() {
        console.log('Engine 2.0 - tr-tr-tr');
    }
};

class EngineV8 {
    complecatedInterface() {
        console.log('Engine V8! - wriim wroom!');
    }
};

// adapter 
class EngineV8Adapter {
    constructor(engine) {
        this.engine = engine;
    }

    simpleInterface() {
        this.engine.complecatedInterface();
    }
};

// --

class Auto {
    startEngine(engine) {
        engine.simpleInterface();
    }
}

// engine 2.0
const myCar = new Auto();
const oldEngine = new Engine2();

myCar.startEngine(oldEngine);

// engine v8 with adapter
const myCarAdap = new Auto();
const engineAdapter = new EngineV8Adapter(new EngineV8());

myCar.startEngine(engineAdapter);


// engine v8 without adapter
const myCarAdapNo = new Auto();
const engineAdapterV8 = new EngineV8();

// myCarAdapNo.startEngine(engineAdapterV8); // error
