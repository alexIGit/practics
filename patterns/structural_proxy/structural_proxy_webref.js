class CarAccess {
    open() {
        console.log('Opening car door!');
    }

    close() {
        console.log('Closing the car door');
    }
}

// proxy
class SecuritySystem {
    constructor(door) {
        this.door = door;
    }

    open(password) {
        if (this.aunthenticate(password)) {
            this.door.open();
        } else {
            console.log('Access denied!');
        }
    }

    aunthenticate(password) {
        return password === 'Ilon';
    }

    close() {
        this.door.close();
    }
};

// ---
const door = new SecuritySystem(new CarAccess());

door.open('Jack');
door.open('Ilon');
door.close();